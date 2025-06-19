import pygame
from typing import List, Dict
import math

from datastructures.graph import Graph, Node
from projects.astar.astar import AStar
from projects.astar.heuristic import HueristicFunction

def main() -> None:
    # Initialize PyGame
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Goonies Treasure Hunt with A* - Interactive")

    # Apply a background image
    background = pygame.image.load("projects/astar/images/map_background.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))

    # Fonts and Colors
    font = pygame.font.SysFont(None, 24)
    WHITE = (255, 255, 255)
    GOLD = (255, 215, 0)
    TRAP_COLOR = (178, 34, 34)
    LINE_COLOR = (200, 200, 200)
    PATH_COLOR = (50, 205, 50)
    TEXT_COLOR = (0, 0, 0)

    # Load assets (Placeholder icons)
    start_icon = pygame.image.load("projects/astar/images/start_icon.png")  # Icon for the start node
    treasure_icon = pygame.image.load("projects/astar/images/treasure_icon.png")  # Icon for the end node
    goonies_icon = pygame.image.load("projects/astar/images/treasure2.png")  # Icon for regular nodes

    trap_icon = pygame.Surface((20, 20))  # Placeholder for trap node
    trap_icon.fill(TRAP_COLOR)

    f_score_display: Dict[Node, float] = {}
    g_score_display: Dict[Node, float] = {}

    nodes = {
        "Start (Astoria)": Node("Start (Astoria)", (100, 200)),
        "Mikey's Hideout (Goondocks)": Node("Mikey's Hideout (Goondocks)", (300, 150)),
        "Pirate's Cove": Node("Pirate's Cove", (500, 300)),
        "Skull Rock": Node("Skull Rock", (600, 400)),
        "Shipwreck Bay": Node("Shipwreck Bay", (400, 500)),
        "Hidden Lagoon": Node("Hidden Lagoon", (200, 450)),
        "Treasure Chest": Node("Treasure Chest", (750, 500))
    }

    # Update connections with pirate-themed descriptions
    nodes["Start (Astoria)"].add_neighbor(nodes["Mikey's Hideout (Goondocks)"], 2.5)
    nodes["Mikey's Hideout (Goondocks)"].add_neighbor(nodes["Pirate's Cove"], 4.0)
    nodes["Pirate's Cove"].add_neighbor(nodes["Skull Rock"], 3.5)
    nodes["Skull Rock"].add_neighbor(nodes["Treasure Chest"], 1.5)
    nodes["Start (Astoria)"].add_neighbor(nodes["Hidden Lagoon"], 5.0)
    nodes["Hidden Lagoon"].add_neighbor(nodes["Shipwreck Bay"], 3.0)
    nodes["Shipwreck Bay"].add_neighbor(nodes["Treasure Chest"], 2.0)
    nodes["Mikey's Hideout (Goondocks)"].add_neighbor(nodes["Shipwreck Bay"], 4.0)

    # Optional: Display brief location descriptions when hovered
    location_descriptions = {
        "Start (Astoria)": "Home base, where the journey begins!",
        "Mikey's Hideout (Goondocks)": "A hidden spot in Astoria, Oregon where the Goonies gather.",
        "Pirate's Cove": "An ancient cove filled with clues and secrets.",
        "Skull Rock": "A treacherous cliffside known for its spooky skull formations.",
        "Shipwreck Bay": "The final resting place of pirate ships, rumored to have treasure!",
        "Hidden Lagoon": "A beautiful yet eerie lagoon hiding traps and treasures.",
        "Treasure Chest": "One-Eyed Willy's legendary treasure chest!"
    }

    # Function to display location descriptions when hovering over a node
    def draw_location_descriptions(mouse_pos):
        for node_name, node in nodes.items():
            if math.dist(mouse_pos, node.position) < 15:  # If hovering over node
                description = location_descriptions[node_name]
                text = font.render(description, True, TEXT_COLOR)
                screen.blit(text, (node.position[0] + 25, node.position[1] - 25))


    # Helper functions
    def draw_nodes():
        for node_name, node in nodes.items():
            # Use start and treasure icons for specific nodes
            if node_name == "Start (Astoria)":
                screen.blit(start_icon, (node.position[0] - start_icon.get_width() // 2, node.position[1] - start_icon.get_height() // 2))
            elif node_name == "Treasure Chest":
                screen.blit(treasure_icon, (node.position[0] - treasure_icon.get_width() // 2, node.position[1] - treasure_icon.get_height() // 2))
            else:
                icon = trap_icon if node.is_trap else goonies_icon
                screen.blit(icon, (node.position[0] - icon.get_width() // 2, node.position[1] - icon.get_height() // 2))

    def draw_edges():
        for node in nodes.values():
            for neighbor, _ in node.neighbors:
                pygame.draw.line(screen, LINE_COLOR, node.position, neighbor.position, 2)

    # Function to display f and g scores
    def draw_node_info():
        for node in nodes.values():
            g_score = g_score_display.get(node, float('inf'))
            f_score = f_score_display.get(node, float('inf'))
            text = font.render(f"{node.name} | f: {f_score:.2f} | g: {g_score:.2f}", True, TEXT_COLOR)
            screen.blit(text, (node.position[0] + 20, node.position[1] - 10))

    # Path recalculation and visualization
    path: List = []

    def recalculate_path(path: List):
        path = AStar.search(Graph(list(nodes.values())), 
                            nodes["Start (Astoria)"], 
                            nodes["Treasure Chest"],
                            HueristicFunction.manhattan_distance,
                            f_score_display,
                            g_score_display)
        
        for i in range(len(path) - 1):
            start_pos = path[i].position
            end_pos = path[i + 1].position
            pygame.draw.line(screen, PATH_COLOR, start_pos, end_pos, 5)
            pygame.draw.circle(screen, PATH_COLOR, start_pos, 6)
            
        pygame.draw.circle(screen, (0, 255, 0), nodes["Treasure Chest"].position, 8)

    # Main loop with description display on hover
    running = True
    dragging = None
    while running:
        screen.blit(background, (0, 0))  # Draw background image
        draw_edges()
        draw_nodes()
        recalculate_path(path)
        draw_node_info()  # Show f and g scores

        mouse_pos = pygame.mouse.get_pos()
        draw_location_descriptions(mouse_pos)  # Display description if hovering

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for node in nodes.values():
                    if math.dist(mouse_pos, node.position) < 15:
                        if event.button == 1:
                            dragging = node
                        elif event.button == 3:
                            node.toggle_trap()

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = None

            elif event.type == pygame.MOUSEMOTION and dragging:
                dragging.position = mouse_pos

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()