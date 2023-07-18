from tkinter import *
import pandas as pd
import tkinter as tk
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
import numpy as np

i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('u.item', sep = '|', names = i_cols, encoding = 'latin-1')

#Train model
class CF(object):
    def __init__(self, Y_data, k, dist_func = cosine_similarity, uuCF = 1):
      self.uuCF = uuCF
      self.Y_data = Y_data if uuCF else Y_data[:, [1, 0, 2]]
      self.k = k
      self.dist_func = dist_func
      self.Ybar_data = None
      

      self.n_users = int(np.max(self.Y_data[:, 0])) + 1
      self.n_items = int(np.max(self.Y_data[:, 1])) + 1

    def add(self, new_data):
      self.Y_data = np.concatenate((self.Y_data, new_data), axis = 0)

    def normalize_Y(self): 
      users = self.Y_data[:, 0]
      self.Ybar_data = self.Y_data.copy()
      self.mu = np.zeros((self.n_users,))
      for n in range(self.n_users):
         ids = np.where(users == n)[0].astype(np.int32)
         item_ids = self.Y_data[ids, 1]
         ratings = self.Y_data[ids, 2]
         m = np.mean(ratings) 
         if np.isnan(m):
               m = 0
         self.mu[n] = m
         self.Ybar_data[ids, 2] = ratings - m

      #Utility matrix, unknow --> 0
      self.Ybar = sparse.coo_matrix((self.Ybar_data[:, 2],
         (self.Ybar_data[:, 1], self.Ybar_data[:, 0])), (self.n_items, self.n_users))
      self.Ybar = self.Ybar.tocsr()

    def similarity_matrix(self): #Similarity_matrix
      self.similarity_mat = self.dist_func(self.Ybar.T, self.Ybar.T)

    def refresh(self):
      self.normalize_Y()
      self.similarity_matrix()
        
    def fit(self):
      self.refresh()
   
    def prediction_rating(self, u, i, normalized = 1):
      ids = np.where(self.Y_data[:, 1] == i)[0].astype(np.int32)
      users_rated_i = (self.Y_data[ids, 0]).astype(np.int32)
      sim = self.similarity_mat[u, users_rated_i]
      a = np.argsort(sim)[-self.k:]
      nearest_s = sim[a]

      r = self.Ybar[i, users_rated_i[a]]
      
      if normalized:
         return int(round((r*nearest_s)[0]/(np.abs(nearest_s).sum() + 1e-8), 0))

      return int(round((r*nearest_s)[0]/(np.abs(nearest_s).sum() + 1e-8) + self.mu[u], 0))

    def pred(self, u, i, normalized = 1):
      if self.uuCF: return self.prediction_rating(u, i, normalized)
      return self.prediction_rating(i, u, normalized)
    
    def pred_array(self, data_test, normalized = 1):
      n_tests = data_test.shape[0]
      arr = []
      for n in range(n_tests):
         pred = self.pred(data_test[n, 0] - 1, data_test[n, 1] - 1, normalized)
         arr.append(pred)
      return np.array(arr)
        
    def recommend(self, u, normalized = 1):
      u = u - 1
      ids = np.where(self.Y_data[:, 0] == u)[0]
      items_rated_by_u = self.Y_data[ids, 1].tolist()              
      recommended_items = {}
      for i in range(self.n_items):
         if i not in items_rated_by_u:
               rating = self.prediction_rating(u, i, normalized = 0)
               if rating > 4: 
                  recommended_items[i + 1] = rating
      aray = []
      for j in recommended_items.keys():
         x = items[items["movie id"] == j]
         aray.append(x["movie title"].iloc[0])
      return aray
         

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
rating_base = pd.read_csv('ub.base', sep = '\t', names = r_cols, encoding = 'latin-1')
rate_train = rating_base.values
rate_train[:, :2] -= 1
model = CF(rate_train, k = 30, uuCF = 1)
model.fit()


#Tkinter
def Take_input():
   global INPUT
   INPUT = inputtxt.get("1.0", "end-1c")
   rs = model.recommend(int(INPUT))
   cnt = 1
   for film in rs:
      T.insert(END, str(cnt) + "." + film + "\n")
      cnt += 1

def refresh():
   T.delete('1.0', 'end')

root = Tk()
canvas1 = tk.Canvas(root, width = 400, height = 500)
canvas1.pack()
lb_root = Label(root, text='Film Recommnended System')
canvas1.create_window(200, 20, window = lb_root)
lb_root.config(font =("Courier", 15))

lb_lst = Label(root, text='LIST FILM')
canvas1.create_window(70, 200, window = lb_lst)
lb_recommed = Label(root, text='FILM RECOMMEND')
canvas1.create_window(270, 200, window = lb_recommed)

mylist = Listbox(root)
for line in range(items.shape[0]):
   mylist.insert(END,  items["movie title"][line])

inputtxt = tk.Text(root, height = 1, width = 10, bg = "light yellow")
canvas1.create_window(210, 90, window = inputtxt)
lb = Label(root, text='User ID')
canvas1.create_window(130, 90, window = lb)


bt1 = tk.Button(root, text = 'Show', command = Take_input)
canvas1.create_window(170, 120, window= bt1)
clear_button = tk.Button(root, text="refresh", command = refresh)
canvas1.create_window(230, 120, window= clear_button)


T = Text(root, height=10, width=30)
canvas1.create_window(270, 300, window = T)
canvas1.create_window(70, 300, window = mylist)
