init -1 python:
    def has_outstanding_notifications():
        return not store.has_updated_apps or not store.has_freed_space or \
            store.sister_request_phase >= 1 and store.sister_request_phase <= 2

    def change_free_space(delta):
        store.free_space += delta
        store.has_seen_space_left_since_last_change = False  # "dirty" free space
