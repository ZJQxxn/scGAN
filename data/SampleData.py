import scanpy.api as sc
import scipy.sparse as sp_sparse

# andata = sc.read_h5ad("./ExprMatrix.h5ad")
andata = sc.read_h5ad("./100_test_data.h5ad")
print("Finished reading.")
andata.var_names_make_unique()
if sp_sparse.issparse(andata.X):
    andata.X = andata.X.toarray()
    # andata = andata
partial_data = andata[:100,:]
print("Finished processing")
sc.write("100_test_data.h5ad", partial_data)
print("Finished writing.")
