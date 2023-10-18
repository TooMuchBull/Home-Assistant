# Home-Assistant

script.verify_scene_applied requires configuration.yaml changes as well as an input boolean (for me input_boolean.scene_match)

configuration.yaml

input_text:
  verify_scene_entity_id:
    name: "Verify Scene Entity ID"

input_number:
  verify_scene_retry_counter:
    name: "Verify Scene Retry Counter"
    min: 0
    max: 10
    step: 1
