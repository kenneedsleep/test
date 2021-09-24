class data_helper:

    def __init__(self,file_name,encoding,path=None):
        self.file_name= file_name
        self.encoding = encoding

    def process(self):
        # import pandas as pd
        # from bs4 import BeautifulSoup
        # import tqdm

        merged =  pd.read_csv(self.file_name,encoding = self.encoding)
        merged['body_content'] =''
        print('Processing start')
        print('total batches: '+ str(merged.shape[0]/100))
        print( 'batch size :', 100)


        for i in tqdm.tqdm(range(merged.shape[0])):
            try:
                soup = BeautifulSoup(merged['body'].iloc[i].replace('\n', ''), features="html.parser")
                merged.loc[i, 'body_content'] = soup.get_text()
            except:
                continue

        return merged

    def save(self):
        data = self.process()
        data.to_csv('processed_'+self.file_name)
    # def run(self):
    #     processes = []
    #
    #     for i in range(1000):
    #         p = mp.Process(target=self.save)
    #         processes.append(p)
    #
    #     [x.start() for x in processes]
if __name__ == "__main__":
    import pandas as pd
    from bs4 import BeautifulSoup
    import tqdm
    # import multiprocessing as mp
    # from time import sleep

    file = data_helper('merged_data.csv','utf-8')
    file.save()