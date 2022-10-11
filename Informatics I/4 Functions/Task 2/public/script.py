#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!


def req_steps(num_disks):
    #      Example case: 4 disks
    # ┌──────────────────────────────────────────────┐
    # │ 1. Move disk 4 from ORIGINAL to GOAL         │
    # │ 2. Move disk 3 from ORIGINAL to EXTRA        │
    # │ 3. Move disk 2 from ORIGINAL to GOAL         │
    # │ 4. Move disk 1 from ORIGINAL to EXTRA   <-END│
    # │ 5. Move disk 1 from EXTRA to GOAL       <-END│
    # │ 6. Move disk 2 from GOAL to EXTRA            │
    # │ 7. Move disk 1 from GOAL to ORIGINAL    <-END│
    # │ 8. Move disk 1 from ORIGINAL to EXTRA   <-END│
    # │ 9. Move disk 3 from EXTRA to GOAL            │
    # │10. Move disk 2 from EXTRA to ORIGINAL        │
    # │11. Move disk 1 from EXTRA to GOAL       <-END│
    # │12. Move disk 1 from GOAL to ORIGINAL    <-END│
    # │13. Move disk 2 from ORIGINAL to GOAL         │
    # │14. Move disk 1 from ORIGINAL to EXTRA   <-END│
    # │15. Move disk 1 from EXTRA to GOAL       <-END│
    # │    For moving 4 disks, 15 steps are required.│
    # └──────────────────────────────────────────────┘
    #  It's 3 steps per recursion.
    #  -> 1 step to move the current disk, and two disks of n-1
    #       -> which also move 1 step and cause two disks of n-1
    #
    # This means we don't simply add 3 steps per disk,
    # but instead, add 1 step and perform bubbling down twice.
    if num_disks == 1:
        return 1
    return 1 + req_steps(num_disks-1) * 2


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("For moving {} disks, {} steps are required.".format(
    4, req_steps(4)))
