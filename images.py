link_start = "https://www.usmint.gov/images/mint_programs/50sq_program/states/"
link_end = "_Designs.gif"

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
          "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
          "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def get_links_list():
    links = []

    for x in states:
        new_link = link_start + x + link_end
        links.append(new_link)

    return links


def get_links_dict():
    dict = {}

    for x in states:
        new_link = link_start + x + link_end
        dict[x] = new_link

    return dict
