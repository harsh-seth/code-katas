class WorkLogItem():
    def __init__(self, position, compensation, start_timestamp, end_timestamp=None) -> None:
        self.position = position
        self.compensation = compensation
        self.start = start_timestamp
        self.end = end_timestamp
        self.ongoing = end_timestamp == None
    
    def record_logout(self, timestamp):
        self.end = timestamp
        self.ongoing = False

class PositionHistoryItem():
    def __init__(self, position, compensation, effective_from_timestamp, prev_post_hist=None) -> None:
        self.position = position
        self.compensation = compensation
        self.effective_from = effective_from_timestamp
        self.prev = prev_post_hist

class EMS():
    def __init__(self) -> None:
        self.work_log = {}
        self.current_pos = {}

    def add_worker(self, worker_id, position, compensation):
        if worker_id in self.current_pos:
            return False
        
        self.current_pos[worker_id] = PositionHistoryItem(position, compensation, 0)
        self.work_log[worker_id] = []
        return True

    def log_work(self, worker_id, timestamp):
        if worker_id not in self.work_log:
            return False
        
        latest_logged_item = self.work_log[worker_id][-1] if len(self.work_log[worker_id]) else None
        if latest_logged_item and latest_logged_item.ongoing:
            latest_logged_item.record_logout(timestamp)
        else:
            applicable_pos = self.current_pos[worker_id]
            while applicable_pos.effective_from > timestamp:
                applicable_pos = applicable_pos.prev

            pos = applicable_pos.position
            comp = applicable_pos.compensation
            self.work_log[worker_id].append(WorkLogItem(pos, comp, timestamp))
        return True

    def calc_time_worked(self, worker_id, position=None):
        if worker_id not in self.work_log:
            return None
        
        time_worked = 0
        for workLogItem in self.work_log[worker_id]:
            if workLogItem.ongoing:
                continue
            if position and workLogItem.position is not position:
                continue
            time_worked += workLogItem.end - workLogItem.start
        return time_worked

    def report_top_n_workers(self, n, position):
        applicable_workers = []
        for worker_id in self.current_pos:
            if self.current_pos[worker_id].position == position:
                applicable_workers.append((worker_id, self.calc_time_worked(worker_id, position)))

        applicable_workers.sort(key=lambda elem: elem[0]) # sort alphabetically
        applicable_workers.sort(key=lambda elem: elem[1], reverse=True) # sort by working hours

        return [f"{elem[0]}({elem[1]})" for elem in applicable_workers[:n]]

    def promote(self, worker_id, new_position, new_compensation, start_timestamp):
        if worker_id not in self.current_pos:
            return False

        current_pos = self.current_pos[worker_id]
        latest_work_item = self.work_log[worker_id][-1] if len(self.work_log[worker_id]) else None
        
        # reject promotion if worker has not started a new shift in newest position yet
        if not latest_work_item or latest_work_item.start < current_pos.effective_from:
            return False

        self.current_pos[worker_id] = PositionHistoryItem(new_position, new_compensation, start_timestamp, current_pos)
        return True

    def calc_salary(self, worker_id, start_timestamp, end_timestamp):
        if worker_id not in self.work_log:
            return None
        
        computed_salary = 0
        for workHistoryItem in self.work_log[worker_id]:
            if workHistoryItem.ongoing:
                continue

            effective_start = max(workHistoryItem.start, start_timestamp)
            effective_end = min(workHistoryItem.end, end_timestamp)
            if effective_end >= effective_start:
                computed_salary += (effective_end - effective_start) * workHistoryItem.compensation
        return computed_salary


ems = EMS()

# Adding new worker
assert ems.add_worker('A', 'Job 1', 1) == True

# Adding existing worker
assert ems.add_worker('A', 'Job 1', 1) == False

# Logging work for non existent worker
assert ems.log_work('Z', 1) == False

# Logging work for worker (login)
assert ems.log_work('A', 1) == True

# Logging work for worker (logout)
assert ems.log_work('A', 2) == True

# Logging work for worker (login)
assert ems.log_work('A', 3) == True

# Calculating time worked for non existent worker
assert ems.calc_time_worked('Z') == None

# Calculating time worked for worker
assert ems.calc_time_worked('A') == 1

# Getting report for top workers for non existent role
assert ems.report_top_n_workers(2, 'Job -1') == []

ems.log_work('A', 5)
ems.add_worker('B', 'Job 1', 1)
ems.add_worker('C', 'Job 1', 1)
ems.add_worker('D', 'Job 1', 1)
ems.add_worker('E', 'Job 2', 1)
ems.log_work('B', 1)
ems.log_work('B', 5)
ems.log_work('C', 2)
ems.log_work('C', 5)
ems.log_work('D', 3)
ems.log_work('D', 4)
ems.log_work('E', 1)
ems.log_work('E', 5)
# Calculating time worked for role
assert ems.report_top_n_workers(3, 'Job 1') == ["B(4)", "A(3)", "C(3)"]

# Promote an employee
assert ems.promote('E', 'Job 3', 5, 6) == True
assert ems.report_top_n_workers(3, 'Job 3') == ["E(0)"]

# Promote an non-existent employee
assert ems.promote('Z', 'Job 3', 5, 6) == False

# Back-to-back promotions
assert ems.promote('E', 'Job 4', 10, 7) == False
assert ems.report_top_n_workers(3, 'Job 4') == []
assert ems.report_top_n_workers(3, 'Job 3') == ["E(0)"]

ems.add_worker('F', 'Job 1', 1)
# "Back-to-back" promotions (new hire with 0 shifts so far)
assert ems.promote('F', 'Job 4', 10, 7) == False

# compute salary for non-existent worker
assert ems.calc_salary('Z', 0, 10) == None

ems.log_work('A', 6)
# compute salary for worker A ((1, 1), (2, 1))
assert ems.calc_salary('A', 0, 10) == 3

# compute salary for worker B ((1, 5))
assert ems.calc_salary('B', 0, 10) == 4

ems.log_work('E', 6)
ems.log_work('E', 8)
# compute salary for worker E ((4, 1), (2, 5))
assert ems.calc_salary('E', 0, 10) == 14

# compute salary between sessions
assert ems.calc_salary('A', 3, 4) == 1
