# Copyright 2026 The MathWorks, Inc.

import json
import os

import pytest

from matlab_proxy.util.list_servers import (
    _extract_version_and_session,
    _get_server_info,
    _get_timestamp,
    _print_server_info_as_table,
    print_server_info,
)


@pytest.fixture
def server_info_file(tmp_path):
    """Creates a temporary mwi_server.info file with sample content."""
    info_file = tmp_path / "mwi_server.info"
    info_file.write_text("http://localhost:12345\nMySession - MATLAB R2024b\n")
    return str(info_file)


@pytest.fixture
def multiple_server_files(tmp_path):
    """Creates multiple temporary mwi_server.info files."""
    files = []
    for i, (url, title) in enumerate(
        [
            ("http://localhost:10000", "Session1 - MATLAB R2024a"),
            ("http://localhost:20000", "Session2 - MATLAB R2024b"),
        ]
    ):
        port_dir = tmp_path / "ports" / str(i)
        port_dir.mkdir(parents=True)
        info_file = port_dir / "mwi_server.info"
        info_file.write_text(f"{url}\n{title}\n")
        files.append(str(info_file))
    return files


# Tests for _extract_version_and_session


class TestExtractVersionAndSession:
    def test_with_session_and_version(self):
        matlab_version, session_name = _extract_version_and_session(
            "MySession - MATLAB R2024b"
        )
        assert matlab_version == "R2024b"
        assert session_name == "MySession"

    def test_without_separator(self):
        matlab_version, session_name = _extract_version_and_session("MATLAB R2024b")
        assert matlab_version == "R2024b"
        assert session_name == ""

    def test_empty_string(self):
        matlab_version, session_name = _extract_version_and_session("")
        assert matlab_version == ""
        assert session_name == ""

    def test_multiple_dashes(self):
        matlab_version, session_name = _extract_version_and_session(
            "My-Session - MATLAB R2024b"
        )
        assert session_name == "My"
        assert matlab_version == "Session"


# Tests for _get_timestamp


class TestGetTimestamp:
    def test_returns_formatted_timestamp(self, server_info_file):
        timestamp = _get_timestamp(server_info_file)
        # Verify the format is dd/mm/yy HH:MM:SS
        from datetime import datetime

        parsed = datetime.strptime(timestamp, "%d/%m/%y %H:%M:%S")
        assert parsed is not None

    def test_timestamp_matches_file_mtime(self, server_info_file):
        from datetime import datetime

        expected_mtime = os.path.getmtime(server_info_file)
        expected = datetime.fromtimestamp(expected_mtime).strftime("%d/%m/%y %H:%M:%S")
        assert _get_timestamp(server_info_file) == expected


# Tests for _get_server_info


class TestGetServerInfo:
    def test_returns_correct_tuple(self, server_info_file):
        timestamp, matlab_version, session_name, address = _get_server_info(
            server_info_file
        )
        assert address == "http://localhost:12345"
        assert matlab_version == "R2024b"
        assert session_name == "MySession"
        # timestamp should be a non-empty string
        assert len(timestamp) > 0

    def test_with_no_session_name(self, tmp_path):
        info_file = tmp_path / "server.info"
        info_file.write_text("http://localhost:9999\nMATLAB R2023a\n")
        timestamp, matlab_version, session_name, address = _get_server_info(
            str(info_file)
        )
        assert address == "http://localhost:9999"
        assert matlab_version == "R2023a"
        assert session_name == ""


# Tests for _print_server_info_as_table


class TestPrintServerInfoAsTable:
    def test_prints_table_with_servers(self, capsys, server_info_file):
        _print_server_info_as_table([server_info_file])
        captured = capsys.readouterr()
        assert "MATLAB Proxy Servers" in captured.out
        assert "http://localhost:12345" in captured.out
        assert "MySession" in captured.out

    def test_prints_no_servers_found_when_empty(self, capsys):
        _print_server_info_as_table([])
        captured = capsys.readouterr()
        assert "No servers found." in captured.out


# Tests for print_server_info


class TestPrintServerInfo:
    def test_quiet_flag(self, capsys, mocker, multiple_server_files):
        mocker.patch(
            "matlab_proxy.util.parse_list_cli_args",
            return_value={"quiet": True, "machine": False, "json": False},
        )
        mocker.patch("glob.glob", return_value=multiple_server_files)
        mocker.patch(
            "matlab_proxy.settings.get_mwi_config_folder",
            return_value=mocker.MagicMock(__truediv__=lambda self, x: self),
        )

        print_server_info()
        captured = capsys.readouterr()
        lines = captured.out.strip().split("\n")
        assert lines == ["http://localhost:10000", "http://localhost:20000"]

    def test_json_flag(self, capsys, mocker, multiple_server_files):
        mocker.patch(
            "matlab_proxy.util.parse_list_cli_args",
            return_value={"quiet": False, "machine": False, "json": True},
        )
        mocker.patch("glob.glob", return_value=multiple_server_files)
        mocker.patch(
            "matlab_proxy.settings.get_mwi_config_folder",
            return_value=mocker.MagicMock(__truediv__=lambda self, x: self),
        )

        print_server_info()
        captured = capsys.readouterr()
        result = json.loads(captured.out)
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0]["server_url"] == "http://localhost:10000"
        assert result[0]["matlab_version"] == "R2024a"
        assert result[0]["session_name"] == "Session1"
        assert "created_on" in result[0]
        assert result[1]["server_url"] == "http://localhost:20000"

    def test_json_flag_empty_servers(self, capsys, mocker):
        mocker.patch(
            "matlab_proxy.util.parse_list_cli_args",
            return_value={"quiet": False, "machine": False, "json": True},
        )
        mocker.patch("glob.glob", return_value=[])
        mocker.patch(
            "matlab_proxy.settings.get_mwi_config_folder",
            return_value=mocker.MagicMock(__truediv__=lambda self, x: self),
        )

        print_server_info()
        captured = capsys.readouterr()
        result = json.loads(captured.out)
        assert result == []

    def test_default_table_output(self, capsys, mocker, multiple_server_files):
        mocker.patch(
            "matlab_proxy.util.parse_list_cli_args",
            return_value={"quiet": False, "machine": False, "json": False},
        )
        mocker.patch("glob.glob", return_value=multiple_server_files)
        mocker.patch(
            "matlab_proxy.settings.get_mwi_config_folder",
            return_value=mocker.MagicMock(__truediv__=lambda self, x: self),
        )

        print_server_info()
        captured = capsys.readouterr()
        assert "MATLAB Proxy Servers" in captured.out
