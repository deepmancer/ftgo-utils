from typing import Dict, Iterable, Tuple, Any

_TEHRAN_POLYGON = {
    "type": "Polygon",
    "coordinates": [[[51.190746, 35.700184], [51.229836, 35.68453], [51.232696, 35.683503], [51.230464, 35.677574], [51.23142, 35.671133], [51.23729, 35.663872], [51.298938, 35.638091], [51.317258, 35.628222], [51.329842, 35.613657], [51.334381, 35.610488], [51.340581, 35.608122], [51.347805, 35.607427], [51.355241, 35.608615], [51.366226, 35.611874], [51.370078, 35.604688], [51.375988, 35.602854], [51.377219, 35.604805], [51.381037, 35.605243], [51.382708, 35.606661], [51.383807, 35.605218], [51.384454, 35.607508], [51.383539, 35.611639], [51.379763, 35.614116], [51.40025, 35.614106], [51.416714, 35.615878], [51.432888, 35.626139], [51.444304, 35.629293], [51.452466, 35.629511], [51.471218, 35.617357], [51.472865, 35.617994], [51.47772, 35.612544], [51.480217, 35.613965], [51.498413, 35.605744], [51.502843, 35.608662], [51.498495, 35.614021], [51.501351, 35.61574], [51.503561, 35.613155], [51.504368, 35.61426], [51.50323, 35.619669], [51.505041, 35.623762], [51.514206, 35.623047], [51.51824, 35.626352], [51.530256, 35.62719], [51.530245, 35.629788], [51.522092, 35.630294], [51.518959, 35.632029], [51.5078, 35.629608], [51.508052, 35.633925], [51.512227, 35.634363], [51.512061, 35.635981], [51.507882, 35.637914], [51.501986, 35.637114], [51.501088, 35.640855], [51.50163, 35.644561], [51.507592, 35.644163], [51.513665, 35.649116], [51.518625, 35.663912], [51.523247, 35.669126], [51.513997, 35.673043], [51.519059, 35.677058], [51.505574, 35.691108], [51.494938, 35.692922], [51.501737, 35.701468], [51.512832, 35.706469], [51.511088, 35.712755], [51.513458, 35.718296], [51.52509, 35.717546], [51.527074, 35.714687], [51.527627, 35.717207], [51.531821, 35.71717], [51.532746, 35.718627], [51.533862, 35.716474], [51.53748, 35.718663], [51.539714, 35.718159], [51.539842, 35.715813], [51.541891, 35.715183], [51.545836, 35.716068], [51.54562, 35.717552], [51.552892, 35.71878], [51.560269, 35.718521], [51.566205, 35.716325], [51.569794, 35.717665], [51.571867, 35.715818], [51.58034, 35.716495], [51.589126, 35.719287], [51.598903, 35.719752], [51.598602, 35.723941], [51.588938, 35.72332], [51.587575, 35.724466], [51.601557, 35.735956], [51.606301, 35.744033], [51.594096, 35.748221], [51.586622, 35.748916], [51.579553, 35.75212], [51.574433, 35.758559], [51.557254, 35.770124], [51.540238, 35.775974], [51.52727, 35.777302], [51.530279, 35.791882], [51.538284, 35.792366], [51.53828, 35.793957], [51.535082, 35.794664], [51.539201, 35.795987], [51.538372, 35.798665], [51.536698, 35.799506], [51.536361, 35.805191], [51.538543, 35.809736], [51.533021, 35.809103], [51.531632, 35.811879], [51.534392, 35.815931], [51.530353, 35.815565], [51.52404, 35.80889], [51.520612, 35.810806], [51.521057, 35.81256], [51.516136, 35.811834], [51.514851, 35.813949], [51.51184, 35.813957], [51.50822, 35.818764], [51.506406, 35.816938], [51.507421, 35.815453], [51.505627, 35.814633], [51.501583, 35.816186], [51.498621, 35.814693], [51.491476, 35.822977], [51.487736, 35.819143], [51.484237, 35.818748], [51.478036, 35.821428], [51.472647, 35.82127], [51.46895, 35.823749], [51.467803, 35.827331], [51.463274, 35.828468], [51.461865, 35.826494], [51.464187, 35.826071], [51.463028, 35.823232], [51.458159, 35.822617], [51.456808, 35.82036], [51.451145, 35.818618], [51.450838, 35.817215], [51.448393, 35.817226], [51.446851, 35.819126], [51.437769, 35.82024], [51.435759, 35.821323], [51.435054, 35.824631], [51.431563, 35.822502], [51.426475, 35.827591], [51.423438, 35.824802], [51.423935, 35.820743], [51.421249, 35.821363], [51.417748, 35.816467], [51.413059, 35.817541], [51.412153, 35.816257], [51.406234, 35.815216], [51.40388, 35.817034], [51.40229, 35.813576], [51.392836, 35.81302], [51.38805, 35.81081], [51.386267, 35.808237], [51.384764, 35.808256], [51.382126, 35.81257], [51.38218, 35.810674], [51.37518, 35.806478], [51.386056, 35.799798], [51.384609, 35.794666], [51.382371, 35.793017], [51.379547, 35.792776], [51.37883, 35.794261], [51.375604, 35.792863], [51.372958, 35.795228], [51.36905, 35.795603], [51.363432, 35.799819], [51.36134, 35.80375], [51.359659, 35.803642], [51.359011, 35.79906], [51.3551, 35.795234], [51.344622, 35.793022], [51.346429, 35.795237], [51.34236, 35.796175], [51.33959, 35.808116], [51.337952, 35.809996], [51.337126, 35.803864], [51.338407, 35.802431], [51.335624, 35.798568], [51.337139, 35.798079], [51.335863, 35.79354], [51.332683, 35.791899], [51.330981, 35.792723], [51.326906, 35.794053], [51.327218, 35.792829], [51.324768, 35.792833], [51.324531, 35.791018], [51.323017, 35.790988], [51.322467, 35.788205], [51.318214, 35.788901], [51.317125, 35.78743], [51.314478, 35.788344], [51.313105, 35.786849], [51.309373, 35.787848], [51.308679, 35.785343], [51.306083, 35.785324], [51.30268, 35.790301], [51.304015, 35.782605], [51.298326, 35.778813], [51.29476, 35.778704], [51.29553, 35.781218], [51.289747, 35.784718], [51.291348, 35.780273], [51.289607, 35.781573], [51.289337, 35.780006], [51.287131, 35.779438], [51.285783, 35.781862], [51.280843, 35.78075], [51.278282, 35.784677], [51.276532, 35.780642], [51.272976, 35.779573], [51.274357, 35.781039], [51.272982, 35.7826], [51.269199, 35.782516], [51.268253, 35.784204], [51.262107, 35.782295], [51.263792, 35.776949], [51.262483, 35.770801], [51.254843, 35.769937], [51.250519, 35.770385], [51.250443, 35.771421], [51.24334, 35.765066], [51.238613, 35.765848], [51.232016, 35.762519], [51.214296, 35.763421], [51.204354, 35.765373], [51.190468, 35.763626], [51.182065, 35.767946], [51.177246, 35.768057], [51.165585, 35.765102], [51.161585, 35.761521], [51.155333, 35.761105], [51.129819, 35.754621], [51.12359, 35.753752], [51.11968, 35.754828], [51.110059, 35.752304], [51.109575, 35.750668], [51.106806, 35.751283], [51.106869, 35.752805], [51.105221, 35.752044], [51.103935, 35.754564], [51.101791, 35.751518], [51.101521, 35.753295], [51.097552, 35.754426], [51.097547, 35.756272], [51.094194, 35.757769], [51.089049, 35.742964], [51.101077, 35.740476], [51.113755, 35.737488], [51.123638, 35.732858], [51.128423, 35.726585], [51.139054, 35.717509], [51.15878, 35.709803], [51.190746, 35.700184]]],
}

_KARAJ_POLYGON = {
    "type": "Polygon",
    "coordinates": [[[51.11879, 35.79154], [51.07457, 35.808812], [51.047128, 35.817346], [51.046596, 35.832158], [51.031524, 35.851926], [51.015421, 35.866421], [51.004434, 35.874221], [50.97745, 35.8888], [50.963039, 35.887762], [50.922347, 35.888477], [50.906249, 35.860049], [50.880389, 35.840368], [50.885131, 35.837809], [50.874135, 35.830089], [50.869679, 35.819751], [50.844868, 35.806014], [50.807939, 35.793144], [50.801751, 35.787033], [50.844184, 35.756141], [50.872002, 35.76021], [50.885649, 35.770443], [50.888662, 35.778947], [50.902291, 35.789701], [50.913784, 35.795701], [50.931936, 35.80166], [50.938439, 35.798981], [50.947788, 35.797849], [50.952137, 35.79531], [50.967545, 35.778874], [50.972547, 35.783147], [50.989216, 35.774657], [50.993152, 35.779961], [50.990238, 35.781476], [50.989891, 35.784043], [50.994647, 35.78877], [51.011342, 35.783487], [51.026951, 35.782598], [51.032159, 35.777655], [51.042327, 35.768669], [51.067916, 35.786142], [51.11879, 35.79154]]],
}

_ISFAHAN_POLYGON = {
    "type": "Polygon",
    "coordinates": [[[51.584446, 32.610738], [51.584734, 32.608625], [51.587329, 32.608838], [51.587426, 32.610593], [51.627003, 32.60413], [51.644916, 32.603673], [51.649912, 32.602278], [51.654648, 32.598577], [51.657998, 32.592818], [51.662621, 32.590688], [51.662252, 32.585552], [51.665796, 32.585109], [51.667352, 32.580889], [51.661366, 32.58029], [51.654753, 32.582467], [51.65222, 32.581471], [51.654801, 32.578779], [51.654661, 32.573799], [51.659551, 32.573823], [51.662083, 32.567122], [51.665277, 32.566061], [51.666402, 32.556832], [51.660456, 32.553138], [51.667504, 32.538092], [51.686556, 32.546961], [51.680344, 32.55978], [51.681669, 32.562121], [51.697634, 32.569188], [51.695374, 32.576187], [51.686928, 32.575082], [51.677426, 32.57035], [51.669621, 32.582611], [51.669341, 32.587209], [51.674264, 32.589434], [51.676111, 32.597152], [51.678233, 32.597993], [51.677769, 32.60394], [51.674608, 32.60489], [51.677392, 32.6092], [51.678582, 32.617724], [51.672422, 32.61849], [51.67251, 32.620789], [51.677963, 32.620495], [51.682281, 32.622823], [51.69186, 32.623863], [51.715931, 32.623894], [51.715931, 32.629125], [51.723355, 32.625709], [51.73434, 32.621843], [51.74684, 32.620181], [51.767268, 32.594182], [51.785545, 32.61103], [51.794561, 32.636936], [51.791022, 32.645037], [51.786708, 32.654161], [51.778926, 32.658555], [51.765007, 32.667023], [51.740471, 32.668589], [51.739929, 32.675718], [51.73649, 32.678361], [51.737406, 32.708349], [51.744839, 32.708682], [51.744839, 32.711641], [51.739824, 32.71139], [51.734056, 32.713697], [51.736012, 32.716305], [51.737467, 32.715202], [51.740175, 32.717459], [51.742482, 32.715202], [51.743435, 32.716004], [51.740735, 32.718463], [51.742398, 32.720132], [51.7352, 32.725475], [51.737193, 32.730569], [51.73258, 32.731495], [51.731857, 32.727965], [51.725679, 32.728432], [51.721277, 32.718798], [51.722203, 32.716224], [51.717923, 32.711147], [51.709607, 32.708274], [51.701592, 32.709749], [51.707111, 32.728846], [51.716365, 32.727624], [51.715727, 32.731081], [51.708078, 32.732546], [51.706782, 32.735148], [51.703046, 32.735307], [51.670947, 32.730806], [51.668342, 32.731422], [51.664362, 32.736163], [51.666497, 32.738345], [51.659793, 32.744042], [51.648755, 32.738448], [51.648983, 32.731264], [51.645235, 32.731683], [51.645033, 32.73015], [51.641054, 32.729482], [51.632793, 32.724662], [51.627472, 32.713644], [51.62137, 32.712007], [51.620528, 32.714604], [51.611337, 32.712524], [51.611735, 32.719102], [51.606595, 32.718651], [51.605862, 32.720166], [51.608688, 32.721979], [51.616513, 32.723273], [51.616587, 32.726673], [51.612661, 32.728094], [51.610991, 32.730599], [51.606231, 32.730869], [51.606163, 32.729854], [51.603659, 32.730102], [51.601702, 32.723987], [51.598004, 32.722558], [51.595684, 32.732829], [51.593731, 32.734682], [51.593764, 32.736277], [51.598005, 32.740052], [51.600148, 32.740034], [51.604832, 32.745919], [51.603008, 32.748989], [51.609457, 32.754334], [51.607878, 32.755936], [51.598108, 32.751853], [51.602004, 32.749185], [51.600022, 32.746943], [51.598131, 32.748198], [51.595401, 32.746595], [51.590459, 32.748243], [51.582599, 32.741245], [51.585551, 32.738941], [51.57717, 32.730824], [51.574237, 32.733193], [51.577757, 32.736668], [51.575952, 32.737819], [51.574237, 32.734502], [51.568619, 32.738608], [51.569657, 32.739939], [51.566786, 32.743702], [51.561978, 32.742852], [51.557898, 32.727489], [51.556034, 32.724657], [51.553291, 32.726059], [51.551892, 32.724254], [51.553607, 32.721637], [51.551892, 32.719019], [51.555269, 32.717368], [51.560736, 32.72772], [51.566253, 32.726586], [51.569809, 32.723265], [51.572785, 32.722728], [51.571669, 32.725858], [51.573034, 32.727899], [51.577631, 32.729327], [51.582671, 32.724105], [51.583873, 32.724812], [51.583853, 32.721573], [51.586641, 32.722465], [51.587724, 32.720359], [51.578157, 32.719096], [51.579992, 32.716418], [51.579057, 32.715019], [51.572681, 32.712677], [51.571919, 32.714765], [51.569662, 32.714173], [51.568674, 32.711577], [51.569944, 32.709179], [51.566897, 32.708728], [51.567151, 32.706753], [51.572492, 32.707304], [51.574994, 32.705568], [51.577251, 32.709433], [51.579406, 32.709985], [51.581399, 32.70839], [51.580715, 32.71001], [51.583908, 32.711304], [51.584224, 32.712789], [51.582217, 32.715171], [51.585326, 32.716776], [51.587754, 32.712518], [51.589919, 32.713355], [51.590765, 32.710674], [51.582865, 32.707571], [51.584361, 32.701816], [51.580059, 32.700695], [51.580661, 32.699266], [51.584874, 32.701335], [51.586868, 32.698626], [51.585928, 32.702012], [51.590103, 32.702238], [51.590404, 32.703404], [51.594429, 32.702463], [51.602592, 32.708407], [51.605, 32.708294], [51.608949, 32.705285], [51.608197, 32.704043], [51.601765, 32.704796], [51.606655, 32.70141], [51.602404, 32.697912], [51.603645, 32.696332], [51.6016, 32.695059], [51.598997, 32.69527], [51.597241, 32.699692], [51.593094, 32.700856], [51.596951, 32.69108], [51.591274, 32.685896], [51.591718, 32.679951], [51.588016, 32.679176], [51.5831, 32.672971], [51.589995, 32.672574], [51.592667, 32.674921], [51.598046, 32.675787], [51.599274, 32.67178], [51.600934, 32.672177], [51.602306, 32.669072], [51.599562, 32.667015], [51.603461, 32.665787], [51.60375, 32.663946], [51.60097, 32.663043], [51.599671, 32.659469], [51.604617, 32.661455], [51.60523, 32.657123], [51.601367, 32.656509], [51.602053, 32.655065], [51.604328, 32.655462], [51.604147, 32.653151], [51.599201, 32.651671], [51.597035, 32.654343], [51.599237, 32.657375], [51.597216, 32.65817], [51.590356, 32.655065], [51.58949, 32.651491], [51.588299, 32.656003], [51.58393, 32.658422], [51.584905, 32.663477], [51.587613, 32.665282], [51.587685, 32.668856], [51.584688, 32.669939], [51.579372, 32.668652], [51.577869, 32.666505], [51.578122, 32.659932], [51.574978, 32.65784], [51.568708, 32.657412], [51.574022, 32.633291], [51.580661, 32.631355], [51.584481, 32.628049], [51.58534, 32.63041], [51.587138, 32.629834], [51.597082, 32.623819], [51.597609, 32.619681], [51.593358, 32.617274], [51.588481, 32.618255], [51.584621, 32.622617], [51.577067, 32.622122], [51.572819, 32.627243], [51.568305, 32.627355], [51.570524, 32.629424], [51.569697, 32.630478], [51.564694, 32.628371], [51.566913, 32.62792], [51.57139, 32.622992], [51.573778, 32.614232], [51.576587, 32.613999], [51.576491, 32.609721], [51.578699, 32.609692], [51.578979, 32.611889], [51.584446, 32.610738]]],
}

_MASHHAD_POLYGON = {
    "type": "Polygon",
    "coordinates": [[[59.721254, 36.24467], [59.72374, 36.251887], [59.717817, 36.256179], [59.712882, 36.256421], [59.704734, 36.251394], [59.69034, 36.257], [59.69378, 36.26285], [59.698952, 36.266948], [59.691795, 36.270304], [59.69717, 36.274453], [59.704943, 36.284758], [59.68297, 36.28033], [59.689751, 36.294513], [59.706573, 36.315177], [59.69988, 36.325128], [59.675463, 36.336262], [59.622539, 36.364889], [59.611024, 36.373483], [59.604075, 36.375585], [59.603442, 36.371485], [59.59838, 36.370581], [59.590015, 36.363142], [59.573791, 36.361749], [59.568407, 36.36271], [59.56682, 36.36093], [59.561048, 36.364398], [59.562072, 36.365652], [59.555811, 36.368417], [59.549664, 36.374782], [59.553503, 36.376504], [59.552794, 36.378458], [59.555574, 36.381432], [59.553426, 36.383879], [59.548777, 36.382835], [59.546592, 36.384935], [59.538233, 36.383258], [59.526669, 36.399307], [59.523615, 36.400863], [59.518926, 36.398007], [59.514331, 36.402212], [59.506261, 36.397442], [59.50034, 36.396521], [59.498027, 36.394807], [59.480888, 36.401841], [59.463241, 36.394292], [59.450081, 36.388289], [59.446922, 36.389946], [59.430778, 36.379849], [59.42026, 36.361849], [59.436602, 36.355199], [59.442499, 36.347264], [59.440564, 36.344584], [59.442383, 36.343246], [59.441965, 36.339785], [59.439747, 36.337628], [59.442066, 36.336387], [59.441146, 36.334871], [59.442927, 36.333342], [59.436115, 36.329638], [59.457594, 36.326439], [59.458434, 36.322556], [59.463392, 36.319655], [59.465332, 36.300571], [59.469212, 36.29343], [59.492149, 36.284513], [59.507292, 36.274808], [59.520249, 36.27172], [59.543681, 36.25936], [59.56251, 36.255771], [59.578405, 36.254507], [59.585241, 36.248227], [59.584151, 36.238673], [59.587841, 36.237511], [59.590609, 36.237178], [59.593828, 36.221806], [59.604923, 36.19682], [59.608215, 36.192736], [59.608677, 36.188346], [59.618212, 36.187252], [59.618405, 36.185371], [59.620693, 36.184576], [59.622434, 36.186926], [59.62119, 36.188279], [59.645933, 36.19464], [59.646076, 36.199023], [59.663104, 36.200632], [59.671853, 36.199831], [59.676458, 36.200794], [59.684009, 36.204934], [59.693228, 36.212923], [59.667222, 36.244071], [59.676734, 36.249653], [59.682003, 36.246237], [59.692614, 36.254528], [59.712878, 36.246644], [59.708023, 36.239595], [59.712152, 36.237974], [59.716042, 36.238121], [59.721254, 36.24467]]],
}

_ARAK_POLYGON = {
    "type": "Polygon",
    "coordinates": [[[49.686629, 34.130686], [49.685348, 34.122732], [49.674257, 34.110194], [49.668675, 34.115338], [49.660456, 34.106368], [49.666582, 34.100594], [49.662967, 34.096205], [49.657602, 34.09608], [49.657087, 34.094837], [49.660049, 34.093593], [49.65977, 34.091496], [49.661486, 34.091016], [49.657656, 34.084805], [49.651283, 34.079456], [49.649878, 34.078763], [49.647571, 34.09194], [49.638762, 34.091811], [49.636284, 34.084771], [49.64027, 34.080306], [49.637994, 34.078707], [49.631048, 34.083392], [49.624019, 34.071605], [49.624815, 34.070702], [49.620416, 34.068605], [49.616076, 34.068547], [49.617412, 34.05993], [49.611238, 34.06416], [49.608207, 34.058597], [49.618013, 34.053157], [49.616597, 34.048677], [49.611468, 34.046312], [49.615223, 34.043423], [49.619965, 34.044046], [49.620762, 34.046521], [49.621983, 34.045806], [49.622766, 34.048366], [49.626768, 34.051299], [49.627052, 34.053402], [49.623485, 34.052535], [49.625727, 34.053957], [49.623667, 34.05482], [49.623474, 34.057246], [49.626521, 34.062659], [49.638312, 34.068196], [49.644706, 34.074275], [49.646691, 34.072578], [49.647109, 34.068565], [49.639878, 34.06936], [49.644148, 34.06361], [49.636533, 34.058695], [49.634089, 34.060278], [49.633527, 34.05641], [49.636359, 34.051237], [49.638408, 34.052775], [49.638559, 34.051584], [49.641219, 34.051184], [49.643086, 34.052562], [49.639941, 34.053836], [49.645033, 34.056673], [49.647635, 34.060188], [49.66316, 34.067307], [49.671442, 34.068098], [49.68269, 34.058504], [49.687686, 34.06361], [49.68745, 34.06585], [49.697428, 34.068027], [49.705378, 34.067236], [49.712105, 34.069849], [49.724464, 34.065743], [49.73103, 34.06585], [49.737489, 34.068712], [49.743068, 34.069352], [49.745107, 34.067929], [49.750624, 34.070436], [49.760921, 34.063272], [49.769547, 34.060606], [49.785683, 34.065022], [49.7835, 34.066124], [49.783709, 34.067734], [49.79403, 34.068303], [49.795583, 34.069587], [49.797077, 34.076799], [49.779353, 34.076888], [49.778645, 34.081668], [49.769588, 34.080253], [49.761059, 34.089501], [49.771113, 34.096063], [49.765045, 34.103024], [49.757059, 34.100558], [49.757574, 34.105], [49.756115, 34.106706], [49.75296, 34.104787], [49.739292, 34.119444], [49.734924, 34.118331], [49.725269, 34.112327], [49.720284, 34.116855], [49.71115, 34.110516], [49.707734, 34.113087], [49.713667, 34.122036], [49.717351, 34.123174], [49.715733, 34.126598], [49.717058, 34.129447], [49.705909, 34.131167], [49.686629, 34.130686]]],
}
    
class Provinces:
    TEHRAN = "TEHRAN"
    KARAJ = "KARAJ"
    ISFAHAN = "ISFAHAN"
    MASHHAD = "MASHHAD"
    ARAK = "ARAK"

    @staticmethod
    def values() -> Iterable[str]:
        for key, value in Provinces.__dict__.items():
            if not key.startswith("__") and not callable(value) and isinstance(value, str):
                yield value

class ProvinceBoundaries:
    # Assuming _TEHRAN_POLYGON, _KARAJ_POLYGON, etc., are defined elsewhere in the code.
    TEHRAN = _TEHRAN_POLYGON
    KARAJ = _KARAJ_POLYGON
    ISFAHAN = _ISFAHAN_POLYGON
    MASHHAD = _MASHHAD_POLYGON
    ARAK = _ARAK_POLYGON

    @staticmethod
    def items() -> Iterable[Tuple[str, Dict[str, Any]]]:
        keys = list(Provinces.values())
        for key in keys:
            yield key, getattr(ProvinceBoundaries, key)

__all__ = ['Provinces', 'ProvinceBoundaries']