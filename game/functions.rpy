init -1 python:
    def has_outstanding_notifications():
        return not has_updated_apps or not has_freed_space or \
            sister_request_phase >= 1 and sister_request_phase <= 2
