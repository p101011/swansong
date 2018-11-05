

def get_blood_source(coords, network):
    # this is going to be an awful implementation
    # revist once blood vessels are handled in engine better
    # think seperate binary search tree would help
    for source_key in network:
        source = network[source_key]
        if len(source.coords) == 1:
            source_center = source.coords[0]
            if abs(coords[0] - source_center[0]) <= source.render_radius:
                if abs(coords[1] - source_center[1]) <= source.render_radius:
                    return source
    return None


def query_renderables(coords, renderable_list):
    for renderable in renderable_list:
        if renderable.rect.collidepoint(coords):
            return renderable
    return None
