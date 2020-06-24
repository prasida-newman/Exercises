import os

def test_solution():
    solution = {}
    for dir_name, subdir_list, file_list in os.walk("3_star_wars"):
    # dir_name, subdir_list, file_list = os.walk(".")
        print(dir_name, subdir_list, file_list)
        solution[dir_name] = file_list

    assert solution == {'3_star_wars': [], 
                        '3_star_wars/tatooine': [], 
                        '3_star_wars/tie_fighter': ['darth_vader.txt'], 
                        '3_star_wars/x_wing': ['luke_skywalker.txt'], 
                        '3_star_wars/millenium_falcon': ['han_solo.txt', 'chewbacca.txt'], 
                        '3_star_wars/the_rebellion': ['leia_organa.txt'], 
                        '3_star_wars/the_empire': []
                        }
