from scipy.stats import norm
from csv import writer

def generate_points(num_points:int=2000):
    distribution_x = norm(loc=0, scale=20)
    distribution_y = norm(loc=0, scale=200)
    distribution_z = norm(loc=0.2, scale=0.05)
    # przy pomocy norm tworzy obiekty reprezentujące\
    # rozkłady prawdopodobieństwa
    # loc=lokalizacja/srednia , scale=odchylenie std.


    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)
    #rvs losuje na podstawie ww. obiektów punty o rozmiarze próbki 2000

    points = zip(x,y,z)
    return points

if __name__ == '__main__':
    cloud_points = generate_points(2000)
    with open('LidarData.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)

        for p in cloud_points:
            csvwriter.writerow(p)