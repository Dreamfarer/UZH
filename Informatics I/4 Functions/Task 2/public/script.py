#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def req_steps(num_disks):
    
    ################################################################
    # Comment by Gianluca
    ################################################################
    # Wikipedia says: 
    # With 3 disks, the puzzle can be solved in 7 moves. 
    # The minimal number of moves required to solve a Tower of Hanoi puzzle is 2^n − 1, where n is the number of disks.
    
    # So we do not actually need to implement the puzzle, we only need to calculate 2^n - 1 without Math.pow()
    
    # Hint: 2^n - 1 can be written as: 1 + 2 * (1 + 2 * (1 + 2 * (...))). Instead of subtracting at the end, we add 1 to every multiplication by 2.
    # Example:
    # 2^4 - 1 = 2 * 2 * 2 * 2 - 1
    # 2^4 - 1 = 1 + 2 * (1 + 2 * (1 + 2 * (1)))
    
    ################################################################
    # Comment & solution by Luca (@LeCarbonator)
    ################################################################

    # Example case: 4 disks
    # ┌──────────────────────────────────────────────┐
    # │ 1. Move disk 4 from ORIGINAL to GOAL         │ <- 1 + ...
    # │                                              │
    # │ 2. Move disk 3 from ORIGINAL to EXTRA        │ <- a
    # │ 3. Move disk 2 from ORIGINAL to GOAL         │ <- a-1
    # │ 4. Move disk 1 from ORIGINAL to EXTRA   <-END│ <- a-1-1 done
    # │ 5. Move disk 1 from EXTRA to GOAL       <-END│ <- a-1-2 done
    # │ 6. Move disk 2 from GOAL to EXTRA            │ <- a-2
    # │ 7. Move disk 1 from GOAL to ORIGINAL    <-END│ <- a-2-1 done
    # │ 8. Move disk 1 from ORIGINAL to EXTRA   <-END│ <- a-2-2 done
    # │                                              │
    # │ 9. Move disk 3 from EXTRA to GOAL            │ <- b
    # │10. Move disk 2 from EXTRA to ORIGINAL        │ <- b-1
    # │11. Move disk 1 from EXTRA to GOAL       <-END│ <- b-1-1 done
    # │12. Move disk 1 from GOAL to ORIGINAL    <-END│ <- b-1-2 done
    # │13. Move disk 2 from ORIGINAL to GOAL         │ <- b-2
    # │14. Move disk 1 from ORIGINAL to EXTRA   <-END│ <- b-2-1 done
    # │15. Move disk 1 from EXTRA to GOAL       <-END│ <- b-2-2 done
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
print("For moving {} disks, {} steps are required.".format(3, req_steps(3)))