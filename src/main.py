import graphs_ex as p1
import bfs_dfs_ex as p2
import dijkstra_ex as p3
import kruskal_prim_ex as p4


def main():
    try:
        #Proyecto 1 - Biblioteca de generación y manejo de grafos
        #p1.graphs_examples()

        #Proyecto_2 _Algoritmos_BFS_y_DFS
        #p2.bfs_dfs_examples()
        
        #Proyecto 3 - Algoritmo de Dijkstra
        #p3.dijkstra_examples()

        #Proyecto 4 - Algoritmos Kruskal y Prim
        p4.kruskal_prim_examples()

    except Exception as err:
        print(err)

main()
