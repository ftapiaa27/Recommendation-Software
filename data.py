calisthenics_skills = ["Planche", "Front Lever", "Back Lever", "Handstand", "Muscle-up", "Human Flag", "V-Sit", "One-arm Pull-up"]

calisthenics_skills = {
    "Planche": "A gymnastics move where the body is held parallel to the ground in a horizontal position, supported only by the hands.",
    "Front Lever": "A gymnastics move where the body is held parallel to the ground in a horizontal position, supported only by the arms.",
    "Back Lever": "A gymnastics move where the body is held parallel to the ground in a horizontal position, supported only by the arms.",
    "Handstand": "A skill where the body is inverted and held up with the hands on the ground.",
    "Muscle-up": "A combination move of a pull-up followed by a dip, where the body is raised up and over a bar or rings.",
    "Human Flag": "A skill where the body is held horizontally parallel to the ground, supported only by the hands on a vertical pole.",
    "V-Sit": "A seated position where the body is lifted off the ground, forming a V shape with the legs and torso.",
    "One-arm Pull-up": "A pull-up performed with only one arm on the bar."
}

planche_progressions = [(1, 'Tuck Planche', 'Start in a push-up position with your hands shoulder-width apart and your fingers pointing forward. Lower your hips and raise your feet, keeping your back straight. Try to hold this position for as long as possible.'),
(2, 'Advanced Tuck Planche', 'From a tucked position, straighten your legs and lift your hips to create a horizontal line with your body.'),
(3, 'Straddle Planche', 'Open your legs into a straddle position, keeping your hips high and your back straight.'),
(4, 'Half-Lay Planche', 'Lower one leg to create a half lay position while keeping the other leg straight and high.'),
(5, 'Full Planche', 'Straighten both legs and lower your body until it is parallel to the ground.'),
(6, 'Planche Push-Ups', 'From a full planche position, lower your body until your chest touches the ground, then push back up to the starting position.')]

front_lever_progressions = [(1, 'Tuck Front Lever', 'Start by hanging from a bar with your knees tucked to your chest. Keep your arms straight and engage your lats to hold your body in a horizontal position.'),
(2, 'Advanced Tuck Front Lever', 'Straighten your legs out in front of you while maintaining a horizontal position.'),
(3, 'Straddle Front Lever', 'Open your legs into a straddle position while keeping your body horizontal.'),
(4, 'Half-Lay Front Lever', 'Lower one leg to create a half lay position while keeping the other leg straight and high.'),
(5, 'Full Front Lever', 'Straighten both legs and hold your body in a horizontal position.'),
(6, 'Front Lever Pull-Ups', 'From a full front lever position, pull your body up to the bar while maintaining a horizontal position.')]

back_lever_progressions = [(1, 'Tuck Back Lever', 'Start by hanging from a bar with your knees tucked to your chest. Keep your arms straight and engage your lats to hold your body in a horizontal position facing the ground.'),
(2, 'Advanced Tuck Back Lever', 'Straighten your legs out in front of you while maintaining a horizontal position facing the ground.'),
(3, 'Straddle Back Lever', 'Open your legs into a straddle position while keeping your body horizontal facing the ground.'),
(4, 'Half-Lay Back Lever', 'Lower one leg to create a half lay position while keeping the other leg straight and high.'),
(5, 'Full Back Lever', 'Straighten both legs and hold your body in a horizontal position facing the ground.'),
(6, 'Back Lever Pull-Ups', 'From a full back lever position facing the ground, pull your body up to the bar while maintaining a horizontal position.')]

Human_Flag_progressions = [
(1, 'Tucked Flag', 'Hold the flag position with your knees tucked into your chest.'),
(2, 'Advanced Tucked Flag', 'Hold the flag position with your knees slightly extended.'),
(3, 'Straddle Flag', 'Hold the flag position with your legs in a straddle position.'),
(4, 'Half-Lay Flag', 'Hold the flag position with your body at a 45 degree angle to the ground.'),
(5, 'Full Flag', 'Hold the flag position with your body parallel to the ground.'),
(6, 'One Arm Human Flag', 'Hold the flag position with only one arm while the other arm hangs by your side.')
]

V_Sit_progressions = [
(1, 'L-Sit', 'Sit on the ground with your legs extended in front of you and lift your body off the ground by pressing your hands into the ground.'),
(2, 'Advanced L-Sit (with feet off ground)', 'Hold the L-Sit position with your feet off the ground.'),
(3, 'V-Sit (with feet on ground)', 'Sit on the ground with your legs extended in front of you and lift your legs off the ground so that your body forms a V shape.'),
(4, 'Straddle V-Sit', 'Sit on the ground with your legs in a straddle position and lift your body off the ground by pressing your hands into the ground.'),
(5, 'Full V-Sit', 'Sit on the ground with your legs extended in front of you and lift your legs off the ground so that your body forms a straight line.'),
(6, 'V-Sit to Handstand', 'From the V-Sit position, press your hands into the ground and lift your body into a handstand position.')
]

One_arm_pull_up_progressions = [
(1, 'Assisted one-arm pull-up', 'Use a resistance band, towel, or partner assistance to assist with the movement.'),
(2, 'One-arm negative pull-up', 'Start at the top of the pull-up position with two hands, then lower yourself down slowly with one arm.'),
(3, 'One-arm scapular pull', 'Hang from a bar with one arm and pull your shoulder blade down towards your hip.'),
(4, 'One-arm flexed arm hang', 'Hold the top position of a one-arm pull-up for time.'),
(5, 'One-arm half pull-up', 'Pull yourself up to the halfway point of a one-arm pull-up, then lower yourself down.'),
(6, 'One-arm pull-up', 'The full one-arm pull-up requires you to pull your body up with only one arm.')
]

handstand_progressions = [
    (1, "Wall Handstand", "Begin in a plank position with your feet against a wall. Walk your feet up the wall and keep your body straight."),
    (2, "Freestanding Handstand (with wall spot)", "Kick up into a handstand with a wall behind you for support. Keep your core engaged and maintain a straight body."),
    (3, "Freestanding Handstand (without wall spot)", "Kick up into a handstand without any support. Keep your core engaged and maintain a straight body."),
    (4, "Handstand Push-Up (against wall)", "From a wall handstand, lower your head down to the ground and push back up."),
    (5, "Handstand Push-Up (freestanding)", "From a freestanding handstand, lower your head down to the ground and push back up."),
    (6, "Handstand Walking", "Walk on your hands while in a handstand position, either with a wall for support or freestanding.")
]

muscleup_progressions = [
    (1, "False Grip Hang", "Hang from a bar with your palms facing towards you and your wrists above the bar."),
    (2, "Muscle-up Transition (with feet on ground)", "Starting from a dead hang, use your legs to assist in pulling yourself up to the transition point."),
    (3, "Muscle-up Transition (with feet elevated)", "Starting from a dead hang, use your legs to assist in pulling yourself up to the transition point, with your feet elevated."),
    (4, "Muscle-up (using resistance bands)", "Loop a resistance band around the bar and use it to assist in the muscle-up movement."),
    (5, "Strict Muscle-up", "Perform a muscle-up with no assistance, relying solely on your upper body strength."),
    (6, "Kipping Muscle-up", "Use a kipping motion to generate momentum to perform the muscle-up.")
]
