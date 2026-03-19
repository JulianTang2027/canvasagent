from dataclasses import dataclass
from enum import Enum

class AssignmentChange(Enum):
    DUE_AT = "due_at"
    LOCK_AT = "lock_at"
    UNLOCK_AT = "unlock_at"

@dataclass
class Change:
    course_id: int
    assignment_id: int
    assignment_name: str
    field: AssignmentChange
    old_value: str | None
    new_value: str | None

def detect_changes(old_state, assignments, course_id):
   
    detected_changes = []

    for assignment in assignments:
        assignment_id = assignment.get("id", -1)
        old_assignment = old_state.get(course_id, {}).get(assignment_id, {})

        for ac in AssignmentChange:
            if old_assignment.get(ac.value, None) != assignment.get(ac.value, None):
                new_Change = Change(
                        course_id=course_id,
                        assignment_id=assignment_id,
                        assignment_name=assignment.get("name", ""),
                        field=ac,
                        old_value=old_assignment.get(ac.value, None),
                        new_value=assignment.get(ac.value, None)
                        )
                detected_changes.append(new_Change)

    return detected_changes
