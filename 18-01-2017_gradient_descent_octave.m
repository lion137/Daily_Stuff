function J = cost_function(Z, y, theta)

% X is a matrix contains trainig examples
% y is a vector of labels
% tehta must be a col vector
m = size(Z, 1); # number of trining examples
%disp(Z)
%disp(theta)
predictions = theta * Z'; # predictios of all hypothesiss fun h(x)
sqr_errors = (predictions - y') .^2; # squared errors

J = 1 / (2 * m) * sum(sqr_errors);

function [G, k] = gradient_descent(X, y, theta, precision, alfa)

% X is a matrix contains trainig examples
% y is a vector of labels
% 
% theta - vector of parameters
% alfa = learning rate
% theta = theta - (alfa / m) * (theta * X(:,:)' - y') * X(:,:);
% 
% 
% for gd theta is row vec, y is column vec X is matrix with added columns of 
% ones from left and rest of columns are training examples
#{
X = 1 1
    1 2
    1 3
#}
con_index = [0];
con_cost = [0];
m = size(X, 1);
i = 0;
control = cost_function(X, y, theta);
while control > precision,
  beg = cost_function(X, y, theta);
   theta = theta - (alfa / m) * (theta  * X' - y') * X;
   an_end = cost_function(X, y, theta);
  control = abs(an_end - beg);
  i += 1;
  con_index = [con_index i];
  con_cost = [con_cost an_end];
  end;
G = theta;
k = i
#i = con_index(1980:2000)
#j = con_cost(1980:2000)



function S = Sum(X, y, theta, ind)
% this function sums to update theta
m = length(X);
i = 1; % sumation index
s = 0; % sum init
while i <= m,
s = s + (theta * X(i, :)' - y(i)) * X(i,ind);
i = i + 1;
end

S = s;



