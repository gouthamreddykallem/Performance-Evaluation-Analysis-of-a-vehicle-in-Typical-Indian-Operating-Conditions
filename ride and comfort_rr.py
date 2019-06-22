
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


df=pd.read_csv("C:\\Users\\preetham\\Desktop\\SIH_Datasets\\WFT_SUV_RR1_R1_.csv")


# In[ ]:


df.columns


# In[ ]:


df.shape


# In[ ]:


df.drop(["SNO"],inplace=True,axis=1)


# In[ ]:


from sklearn.preprocessing import StandardScaler


# In[ ]:


normalizedata=df


# In[ ]:


X=df[[ 'TIME', 'Veh_Speed', 'CS_RR', 'CS_RL', 'ARB_R', 'AXLE_RR_Z',
       'AXLE_RL_Z', 'RR_Mz', 'pca', 'RR_Mx', 'RR_Fz', 'RR_Fy', 'RR_Fx',
       'RL_Mz', 'RL_Mx', 'RL_Fz', 'RL_Fy', 'RL_Fx', 'RRA_Z', 'RLA_Z', 'CG_X',
       'CG_Y', 'CG_Z' ]]


# In[ ]:


def Normalization(num):
    normalizedata[X.columns[i]]=StandardScaler().fit_transform(df[X.columns[i]].values.reshape(-1,1))
for i in range(0,20):
    Normalization(i)


#  type(df)

# In[ ]:


from sklearn.cluster import KMeans


# In[ ]:


kmeans=KMeans(n_clusters=2)


# In[ ]:


kmeans.fit(df)


# In[ ]:


count1=0
count2=0
for i in kmeans.labels_:
    if i==1:
        count1=count1+1
    elif i==0:
        count2=count2+1


# In[ ]:


import seaborn as sn
k=list()
for i in kmeans.labels_:
    k.append(i)
k=pd.DataFrame(k,columns=["clusters"])


# In[ ]:


sn.distplot(k["clusters"],kde=False,color="red")


# In[ ]:


count1


# In[ ]:


count2


# In[ ]:


import numpy as np
clusters=kmeans.fit_predict(df)


# In[ ]:


cluster_0=np.where(clusters==0)
cluster_1=np.where(clusters==1)


# In[ ]:


from nltk.cluster import KMeansClusterer, euclidean_distance


# In[ ]:


df=df.values


# In[ ]:


x_cluster_0=df[cluster_0]
x_cluster_1=df[cluster_1]


# In[ ]:


ls=list()
ls1=list()


# In[ ]:


for i in range(0,48829):
    
    distance=euclidean_distance(x_cluster_0[i],kmeans.cluster_centers_[0])
    ls.append(distance)


# In[ ]:


for i in range(0,97364):
    distance=euclidean_distance(x_cluster_1[i],kmeans.cluster_centers_[1])
    ls1.append(distance)


# In[ ]:


min(ls)


# In[ ]:


max(ls)


# In[ ]:



mn=1.1281895289261281
mx=20.956514229666816


# In[ ]:


l1=list()
for i in ls:
    print('score :{}'.format((i-mn)/(mx-mn)))
    l1.append((i-mn)/(mx-mn)*10)


# In[ ]:


min(ls1)


# In[ ]:


max(ls1)


# In[ ]:


mn1=1.3893177960708116


# In[ ]:


mx1=17.545120971277715


# In[ ]:



l2=list()
for i in ls1:
    print('score :{}'.format((i-mn1)/(mx1-mn1)))
    l2.append((i-mn1)/(mx1-mn1)*10)


# In[ ]:


l1=pd.DataFrame(l1,columns=["cluster_0"])


# In[ ]:


sn.distplot(l1["cluster_0"],kde=False,color="red")


# In[ ]:


l2=pd.DataFrame(l2,columns=["cluster_1"])


# In[ ]:


sn.distplot(l2["cluster_1"],kde=False,color="red")

