from DrawFile import Draw

def main():
    
    Dr =  Draw()
    Dr.draw_small_square(100, 100, Dr.green)
    Dr.draw_frame_by_sup_left_corner(100, 100, 100, 100, Dr.red)
    Dr.draw_frame_by_center(100, 100, 100, 100, Dr.green)
    #Dr.draw_frame_by_sup_left_corner(100, 100, 100, 100, Dr.red)
    #Dr.draw_frame_by_center(100, 100, 100, 100, Dr.red)



if __name__ == "__main__":
    main()