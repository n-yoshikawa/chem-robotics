(define (domain xdl)
  (:requirements :negative-preconditions :strips :typing)
  (:types beaker)
  (:predicates
      (hand_available)
      (picked ?reagent - beaker)
      (occluded ?target - beaker ?obstacle - beaker)
      (moved ?vessel - beaker ?reagent - beaker)
      (added ?vessel - beaker ?reagent - beaker)
      (stiring ?vessel - beaker)
  )
  
  (:action remove
   :parameters (?obstacle - beaker ?target - beaker )
   :precondition (and (picked ?obstacle) (occluded ?target ?obstacle))
   :effect (and (not (occluded ?target ?obstacle)) 
                (not (picked ?obstacle))
                (hand_available))
  )

  (:action pick
   :parameters (?reagent - beaker)
   :precondition (and 
                  (hand_available)
                  (forall (?b - beaker) (not (occluded ?reagent ?b))))
   :effect (and (picked ?reagent) (not (hand_available)))
  )

  (:action move
   :parameters (?vessel - beaker ?reagent - beaker)
   :precondition (picked ?reagent)
   :effect (moved ?vessel ?reagent)
  )

  (:action pour
   :parameters (?vessel - beaker ?reagent - beaker)
   :precondition (and (picked ?reagent)
                      (moved ?vessel ?reagent)
                      (not (stiring ?vessel))
                      (not (added ?vessel ?reagent)))
   :effect (and (added ?vessel ?reagent))
  )

  (:action place
   :parameters (?reagent - beaker)
   :precondition (picked ?reagent)
   :effect (and (not (picked ?reagent)) (hand_available))
  )
)
