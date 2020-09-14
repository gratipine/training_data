###### FLOW file
# this dictinobary contains information for what type of ticket there is. 
dict_flow_records = {
    "record_type": "F",
    "length": 49,
    "records": {
    "update_marker": (0, 1),
    "record_type": (1, 2),
    "origin_code": (2, 6),
    "destination_code": (6, 10),
    "route_code": (10, 15),
    "status_code": (15, 18), 
    "usage_code": (18, 19),
    "direction": (19, 20),
    "end_date": (20, 28),
    "start_date": (28, 36),
    "toc": (36, 39), 
    "cross_london_ind": (39, 40),
    "non_standard_disc_ind": (40, 41),
    "publication_ind": (41, 42),
    "flow_id": (42, 49)
    }
}

# this dictionary holds the information for for what the fares are for the different types
# it joins to the previous one by the flow_id
dict_fare_records = {
    "record_type": "T",
    "length": 22,
    "records": {
    "update_marker": (0, 1),
    "record_type": (1, 2),
    "flow_id": (2, 9),
    "ticket_code": (9, 12),
    "fare": (12, 20), # in pence
    "restriction_code": (20, 22)
    }
}


#### Locations file
dictionary_locations = {
    "record_type": "L",
    "length": 289,
    "records": {
    "update_marker": (0, 1),
    "record_type": (1, 2),
    "uic_code": (2, 9),
    "end_date": (9, 17), 
    "start_date": (17, 25),
    "quote_date": (25, 33),
    "admin_area_code": (33, 36),
    "nlc_code": (36, 40),
    "description": (40, 56),
    "crs_code": (56, 59),
    "resv_code": (59, 64),
    "ers_country": (64, 66),
    "ers_code": (66, 69),
    "fare_group": (69, 75),
    "county": (75, 77),
    "pte_code": (77, 79),
    "zone_no": (79, 83),
    "zone_ind": (83, 85),
    "region": (85, 86),
    "hierarchy": (86, 87),
    "cc_desc_out": (87, 128),
    "cc_desc_rtn": (128, 144),
    "atb_desc_out": (144, 204),
    "atb_desc_rtn": (204, 234),
    "special_facilities": (234, 260),
    "lul_direction_ind": (260, 261),
    "lul_uts_mode": (261, 262),
    "lul_zone_1": (262, 263),
    "lul_zone_2": (263, 264),
    "lul_zone_3": (264, 265),
    "lul_zone_4": (265, 266),
    "lul_zone_5": (266, 267),
    "lul_zone_6": (267, 268),
    "lul_uts_london_stn": (268, 269),
    "uts_code": (269, 272),
    "uts_a_code": (272, 275),
    "uts_ptr_bias": (275, 276),
    "uts_offset": (276, 277),
    "uts_north": (277, 280),
    "uts_east": (280, 283),
    "uts_south": (283, 286),
    "uts_west": (286, 289)
    }
}


dict_associated_stations = {
    "record_type": "M", #A
    "length": 27, 
    "records": {
    "update_marker": (0, 1),
    "record_type": (1, 2),
    "uic_code": (2, 9),
    "end_date": (9, 17),
    "assoc_uic_code": (17, 24),
    "assoc_crs_code": (24, 27)
    }
}

dict_railcard_geography = {
    "record_type": "R",
    "length": 20,
    "records": {
    "update_marker": (0, 1),
    "record_type": (1, 2),
    "uic_code": (2, 9),
    "railcard_code": (9, 12),
    "end_date": (12, 20)
    }
}

dict_synonym = {
    "record_type": "S",
    "length": 41,
    "records": {
    "update_marker": (0, 1),
    "record_type": (1, 2),
    "uic_code": (2, 9),
    "end_date": (9, 17),
    "start_date": (17, 25),
    "description": (25, 41)
    }
}

#### Routes file
dict_routes = {
    "record_type": "R",
    "length": 263,
    "records": {
    "update_marker": (0, 1),
    "record_type": (1, 2), #R
    "route_code": (2, 7),
    "end_date": (7, 15),
    "start_date": (15, 23),
    "quote_date": (23, 31),
    "description": (31, 47) 
    }
}

dict_route_exclusions = {
    "record_type": "L",
    "length": 26,
    "records": {
    "update_marker": (0, 1),
    "record_type": (1, 2), #L
    "route_code": (2, 7),
    "end_date": (7, 15),
    "admin_area_code": (15, 18),
    "nlc_code": (18, 22), #national location code
    "crs_code": (22, 25), 
    "incl_excl": (25, 26)
    }
}