# Here in Utilities , we will write those functions or transformations which we are going to user again and again

class reusable:

  def dropColumns(self, df, columns):
    return df.drop(*columns)