// Copyright 2024-2025 The MathWorks, Inc.

// Time Interval in milliseconds between subsequent 'get_status' requests
export const STATUS_REQUEST_INTERVAL_MS = 1000;

// Maximum number of consecutive failed requests allowed before triggering a connection error
export const MAX_REQUEST_FAIL_COUNT = 60;
export const MWI_AUTH_TOKEN_NAME_FOR_HTTP = 'mwi-auth-token';

// Buffer timer duration in seconds after the IDLE timer expires
export const BUFFER_TIMEOUT_DURATION = 10;
