# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas,scene_width,scene_height)
    draw_clouds(canvas, 400,400,350,370)
    draw_road(canvas, scene_width,scene_height)
    draw_road_lines(canvas,415,400)
    
    draw_clouds(canvas, scene_width - 100, scene_height - 200, scene_width - 150, scene_height - 225)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):

    draw_rectangle(canvas, 0, scene_height/3,
        scene_width, scene_height, width=0, fill="sky blue")

def draw_clouds(canvas,cloud_x1,cloud_y1,cloud_x2,cloud_y2):
    draw_oval(canvas, cloud_x1,cloud_y1,cloud_x2,cloud_y2, fill= "white", width= 0)
    draw_oval(canvas, cloud_x1+15,cloud_y1,cloud_x2+30,cloud_y2, fill="white", width=0)    

def draw_ground(canvas,scene_width,scene_height):
    draw_rectangle(canvas,0, 0, scene_width, scene_height/3, width=0,  fill ="green")

def draw_road(canvas, scene_width, scene_height):
    draw_rectangle(canvas,300, 0, scene_width/1.5, scene_height/3, width=0,  fill ="black")

#road lines different sizes on purpose
def draw_road_lines(canvas,line_width_min,line_width_max):
    draw_rectangle(canvas, line_width_min,20,line_width_max,50, fill = "yellow", width=1) 
    draw_rectangle(canvas, line_width_min,60,line_width_max,80, fill = "yellow", width=1) 
    draw_rectangle(canvas, line_width_min,90,line_width_max,120, fill = "yellow", width=1) 
    draw_rectangle(canvas, line_width_min,130,line_width_max,150, fill = "yellow", width=1) 


# Call the main function so that
# this program will start executing.
main()


