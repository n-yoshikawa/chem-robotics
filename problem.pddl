(define (problem tmp)
  (:domain xdl)
  (:objects glass - beaker water - beaker vodka - beaker gin - beaker)
  (:init (hand_available) (occluded vodka gin))
  (:goal 
    (and (hand_available) (added glass vodka))
  )
)
