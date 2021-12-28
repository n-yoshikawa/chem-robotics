(define (domain xdl)
    (:requirements :negative-preconditions)

  (:predicates
      (hand_available)
      (picked ?reagent)
      (moved ?vessel ?reagent)
      (added ?vessel ?reagent)
      (stiring ?vessel)
  )
  
  (:action pick
   :parameters (?reagent)
   :precondition (hand_available)
   :effect (and (picked ?reagent) (not (hand_available)))
  )

  (:action move
   :parameters (?vessel ?reagent)
   :precondition (picked ?reagent)
   :effect (moved ?vessel ?reagent)
  )

  (:action pour
   :parameters (?vessel ?reagent)
   :precondition (and (picked ?reagent)
                      (moved ?vessel ?reagent)
                      (not (stiring ?vessel))
                      (not (added ?vessel ?reagent)))
   :effect (and (added ?vessel ?reagent))
  )

  (:action pour_and_stir
   :parameters (?vessel ?reagent)
   :precondition (and (moved ?vessel ?reagent)
                      (stiring ?vessel)
                      (not (added ?vessel ?reagent)))
   :effect (and (added ?vessel ?reagent))
  )

  (:action place
   :parameters (?reagent)
   :precondition (picked ?reagent)
   :effect (and (not (picked ?reagent)) (hand_available))
  )
)
