classdef TransportMap
    %UNTITLED2 Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
      N; % dimension of input and output space
      K; % maximum degree of polynomial
      H_z ; % (N by K+1 ) - univariate basis evaluated (dimension, order)
      dH_z; % (N by K+1 ) = gradient of basis evaluated (dimension, order)

      
    end
    
    methods
         function tm = TransportMap(N,K)
            if (nargin > 0)
                tm = TransportMap;               
                tm.N = N;
                tm.K = K;
                tm.H_z = zeros(N,K+1);
                tm.dH_z = zeros(N,K+1);
            end
        end %end constructor
        
        function fit_sample(tm,z)
            for n = 1 : tm.N
                for l = 1 : tm.K + 1
                    
                end
            end
        end
        
        
    end
    
end

