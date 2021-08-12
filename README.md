# Model-Selection
Consider a situation when you have an already released video segmentation model and there are 3 new candidates for the next release. The new models consume significantly low CPU compared to the released one. The only concern is that the quality of the new models may be worse than the released one and they may not be accepted for the release solely due to bad segmentation quality. You need to decide if the new models are good enough for the release and if yes - which one is the best. There is an objective evaluation metric called IoU (Intersection over Unit) that the team uses to compare the models. You have the evaluation results on ~100 video files (in the attached files). Try to find out the best model based on these evaluations and decide if that's a good release candidate or not.


P.S.

Due to lack of time I didn՛t have time to delete the "Evaluation results: IoU: ..."  in code, please delete the "Evaluation results: IoU: ..." from .log files.
I didn't do interactive path input feature using argparse, but know that it will be better.
