# Bayesian Hierarchical Analysis of Esophageal Cancer Risk Factors: Evaluating the Role of Age, Tobacco, and Alcohol Consumption
Course project for CS-E5710 - Bayesian Data Analysis D

Modeling the likelihood of developing Esophageal Cancer from a Bayesian perspective

Author: Quan Tran and Krzysztof Modrzyński


## Introduction

This project is part of the Aalto University Bayesian Data Analysis 2023 Course. 

Esophageal cancer is cancer in the esophagus -- the food pipe connecting the throat and the stomach. In recent years, esophageal cancer has been among the most common types of cancer: in 2020, it ranked 8th in the most diagnosed type of cancer globally, with 604,000 new cases. It is also the 6th most deadly cancer killing over 544,000 people in 2020.

Smoking and alcohol use have long been known as two major risk factors associated with esophageal cancer, and they are among the few risk factors that can be controlled or changed by the subject. The goal of this project is to utilize Bayesian modeling to the data from a case-control study of esophageal cancer in hopes of drawing a relation between a person's level of tobacco and alcohol intake and their chance of developing esophageal cancer. Our modelling will also account for the patients' age as that is an important factor in the development of cancers.

## Data description
Our data set was created by Tuyns AJ, Péquignot G, Jensen OM. in a paper *Esophageal cancer in Ille-et-Vilaine about levels of alcohol and tobacco consumption. Risks are multiplying. (1977).*

The data set contains the following columns:

1.  **`agegp`**: Age group

2.  **`alcgp`**: Alcohol consumption group

3.  **`tobgp`**: Tobacco consumption group

4.  **`ncases`**: Number of cases

5.  **`ncontrols`**: Number of controls

6.  **`total`**: Total number of subjects

7.  **`prob`**: Empirical probability
