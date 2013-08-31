#!/bin/bash
#Aug232013sw

#The included 3class model in NER assumes PERSON for PERS, ORGANIZATION for ORG, and LOCATION for LOC.  used replace-all in NP++ to format control tsv files.
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ./ner/classifiers/english.all.3class.distsim.crf.ser.gz -testFile ./ctrlformattsv/1.tsv > ctrl1
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ./ner/classifiers/english.all.3class.distsim.crf.ser.gz -testFile ./ctrlformattsv/2.tsv > ctrl2
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ./ner/classifiers/english.all.3class.distsim.crf.ser.gz -testFile ./ctrlformattsv/3.tsv > ctrl3
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ./ner/classifiers/english.all.3class.distsim.crf.ser.gz -testFile ./ctrlformattsv/4.tsv > ctrl4
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ./ner/classifiers/english.all.3class.distsim.crf.ser.gz -testFile ./ctrlformattsv/5.tsv > ctrl5
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ./ner/classifiers/english.all.3class.distsim.crf.ser.gz -testFile ./ctrlformattsv/6.tsv > ctrl6
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ./ner/classifiers/english.all.3class.distsim.crf.ser.gz -testFile ./ctrlformattsv/7.tsv > ctrl7
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ./ner/classifiers/english.all.3class.distsim.crf.ser.gz -testFile ./ctrlformattsv/8.tsv > ctrl8
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ./ner/classifiers/english.all.3class.distsim.crf.ser.gz -testFile ./ctrlformattsv/9.tsv > ctrl9
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ./ner/classifiers/english.all.3class.distsim.crf.ser.gz -testFile ./ctrlformattsv/10.tsv > ctrl10

#Testing models trained on clean files
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-clean/sans1.ser.gz -testFile ./cleanedtsv/1.tsv > ./results/clean1
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-clean/sans2.ser.gz -testFile ./cleanedtsv/2.tsv > ./results/clean2
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-clean/sans3.ser.gz -testFile ./cleanedtsv/3.tsv > ./results/clean3
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-clean/sans4.ser.gz -testFile ./cleanedtsv/4.tsv > ./results/clean4
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-clean/sans5.ser.gz -testFile ./cleanedtsv/5.tsv > ./results/clean5
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-clean/sans6.ser.gz -testFile ./cleanedtsv/6.tsv > ./results/clean6
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-clean/sans7.ser.gz -testFile ./cleanedtsv/7.tsv > ./results/clean7
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-clean/sans8.ser.gz -testFile ./cleanedtsv/8.tsv > ./results/clean8
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-clean/sans9.ser.gz -testFile ./cleanedtsv/9.tsv > ./results/clean9
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-clean/sans10.ser.gz -testFile ./cleanedtsv/10.tsv > ./results/clean10

#Testing models trained on raw gold-std files
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-inc/without-one/withoutonemodel.ser.gz -testFile ./cleanedtsv/1.tsv > ./results/inc1
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-inc/without-two/withouttwomodel.ser.gz -testFile ./cleanedtsv/2.tsv > ./results/inc2
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-inc/without-three/withoutthreemodel.ser.gz -testFile ./cleanedtsv/3.tsv > ./results/inc3
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-inc/without-four/withoutfourmodel.ser.gz -testFile ./cleanedtsv/4.tsv > ./results/inc4
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-inc/without-five/withoutfivemodel.ser.gz -testFile ./cleanedtsv/5.tsv > ./results/inc5
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-inc/without-six/withoutsixmodel.ser.gz -testFile ./cleanedtsv/6.tsv > ./results/inc6
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-inc/without-seven/withoutsevenmodel.ser.gz -testFile ./cleanedtsv/7.tsv > ./results/inc7
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-inc/without-eight/withouteightmodel.ser.gz -testFile ./cleanedtsv/8.tsv > ./results/inc8
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-inc/without-nine/withoutninemodel.ser.gz -testFile ./cleanedtsv/9.tsv > ./results/inc9
java -cp ./ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ../trained-classifiers/fixed-inc/without-ten/withouttenmodel.ser.gz -testFile ./cleanedtsv/10.tsv > ./results/inc10
