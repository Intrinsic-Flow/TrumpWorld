import csv

default_paths = ["../data/org-org-connections.csv",
					"../data/person-org-connections.csv",
					"../data/person-person-connections.csv" ]

def extract_set_from_csv(input_file, column_list):
	inpf = open(input_file)
	inpf.readline()
	f = csv.reader(inpf)
	result = set()
	for line in f:
		for n in column_list:
			result.add(line[n])
	return result

def graqlize_entities(p_p=default_paths[2],
					p_o=default_paths[1],
					o_o=default_paths[0],
					output_path="entities.gql"):
	people = extract_set_from_csv(p_p,[0,1])
	orgs = extract_set_from_csv(o_o,[0,1])
	people = people.union(extract_set_from_csv(p_o,[1]))
	orgs = orgs.union(extract_set_from_csv(p_o,[0]))
	outf = open(output_path, "w")
	for p in people:
		s = "insert $p isa person, has name '" + p.replace("\'","\\'") + "';\n"
		outf.write(s)
	for o in orgs:
		s = "insert $p isa organisation, has name '" + o.replace("\'","\\'") + "';\n"
		outf.write(s)
	outf.close()

def graqlize_assertion(input_line, role_map, role_players, relation_type):
	s = "match $x isa " + role_players[0] + ", has name '" +  input_line[0].replace("\'","\\'") + "';\n"
	s += "$y isa " + role_players[1] + ", has name '" + input_line[1].replace("\'","\\'") + "';\n"
	s += "insert (" + role_map[0] + ": $x, " + role_map[1] + ": $y) isa " + relation_type
	s += ", has description '" + input_line[2].replace("\'","\\'") + "'"
	s += ", has source '" + input_line[3] + "';\n"
	return s

def graqlize_relations(p_p=default_paths[2],
					p_o=default_paths[1],
					o_o=default_paths[0],
					output_path="relations.gql"):
	outf = open(output_path,"w")
	passes = [[p_p, ["person-a", "person-b"], ["person", "person"], "person-person"],
			[o_o, ["organisation-a", "organisation-b"], ["organisation", "organisation"], "organisation-organisation"],
			[p_o, ["organisation-connection", "person-connection"], ["organisation", "person"], "person-organisation"]]
	for p in passes:
		inpf = open(p[0])
		inpf.readline()
		cr = csv.reader(inpf)
		for l in cr:
			res = graqlize_assertion(l, p[1], p[2], p[3])
			outf.write(res)
		inpf.close()
	outf.close()
