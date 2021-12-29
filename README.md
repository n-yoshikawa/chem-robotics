1. Generate `problem.pddl` by running `xdl_to_pddl.py`.
```
python xdl_to_pddl.py procedure.xdl
```
Three problems corresponding three actions in XDL will be generated. Save one of them as `problem.pddl`

```
(define (problem tmp)
  (:domain xdl)
  (:objects beaker red_cabbage_soup baking_soda_solution vinegar)
  (:init (hand_available))
  (:goal 
    (and (hand_available) (added beaker vinegar))
  )
)
```

2. Solve the problem by `pddl_solver.py`
```
python pddl_solver.py domain.pddl problem.pddl plan.ipc
```

Plan for the problem will be generated in `plan.ipc`.

```
(pick vinegar)
(move beaker vinegar)
(pour beaker vinegar)
(place vinegar)
```

# MoveIt
Follow the [Python tutorial](https://ros-planning.github.io/moveit_tutorials/doc/move_group_python_interface/move_group_python_interface_tutorial.html)

replace `move_group_python_interface_tutorial.py` in `ws_moveit`.

