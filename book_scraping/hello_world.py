import luigi
import os, sys
from abc import ABC, abstractmethod
from time import sleep
import datetime
from random import choice


class TaskTemplate(luigi.Task):
    def __init__(self):
        super().__init__()
        self.data = {
            'app_name' : str(__class__.__name__),
            'file_name':  'stub__'+ str(__class__.__name__) +'.txt',
            'exec_secs': 0,
            'random': choice(range(2, 10))
        }


    @abstractmethod
    def requires(self) -> list:
        pass

    @abstractmethod
    def output(self):
        return luigi.LocalTarget(self.data['file_name'])

    
    @abstractmethod
    def run(self):
        sleep(self.data['exec_secs'])
        print("Writing the output File ...")
        with self.output().open("w") as outfile:
            outfile.write("Started At: {}\n".format(datetime.datetime.now()))
            outfile.write("Runing the app:{}\n".format(self.data['app_name']))
            outfile.write("Ran for {} seconds...\n".format(self.data['exec_secs']))
            outfile.write("Computed Value: {}\n".format(self.data['random']))




class Init(TaskTemplate):
    override = luigi.IntParameter(default=3)
    def __init__(self):
        super().__init__()
        delay = choice(range(2, 10))
        
        if self.override:
            if self.override < 10:
                print("Init will run for user defined seconds:", self.override)
                delay = self.override
            else:
                print("User defined ovcerride is big.. so sticking to default")
        self.data = {
            'app_name' : str(__class__.__name__),
            'file_name':  'stub__'+ str(__class__.__name__) +'.txt',
            'exec_secs': 3,
            'random': delay
        }


    def requires(self) -> list:
        return super().requires()
    
    def output(self):
        return super().output()
        
    
    def run(self):
        super().run()
        print("Override value is:", self.override)

# To execute
# python -m luigi --local-scheduler --module hello_world Init