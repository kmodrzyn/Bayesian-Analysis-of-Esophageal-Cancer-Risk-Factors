data {
    // number of data points
    int<lower=0> N;
    
    vector[N] alc; // alcohol
    vector[N] tob; // tobacco
    vector[N] age; // age
    array[N] int cancer;
  
}
transformed data {
  vector[N] alc_std = (alc - mean(alc)) / sd(alc);
  vector[N] tob_std = (tob - mean(tob)) / sd(tob);
  vector[N] age_std = (age - mean(age)) / sd(age);
}
parameters {
  
    real alpha;
    real beta;
    real gamma;
    real delta;
    

}
transformed parameters {
  vector[N] theta = alpha + beta * alc_std + gamma * tob_std + delta * age_std;
}
model {
    // Model is prior sensitive.
    alpha ~ normal(0, 1);
    beta ~ normal(0, 1);
    gamma ~ normal(0, 1);
    delta ~ normal(0, 1);
    
    cancer ~ bernoulli_logit(theta);
}
generated quantities {
  array[N] int y_pred;
  y_pred = bernoulli_logit_rng(theta);
}