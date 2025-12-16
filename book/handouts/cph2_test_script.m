
% First simulation run: fo = 1000, fs = 8000, Amplitude = 5, cycles = 10
samples = cph2_lastname(1000,8000,5,10);
fprintf(1,'simulation 1, fo = 1000, fs = 8000, Amplitude = 5, cycles = 10');
fprintf(1,'\n');
fprintf(1,'length of samples  ');
fprintf(1,'%d', length(samples));
fprintf(1,'\n');
fprintf(1,'hit the space bar to continue');
fprintf(1,'\n');
pause; % hit the space bar to continue
close all;
% Second simulation run: fo = 1000, fs = 1000, Amplitude = 5, cycles = 10
samples = cph2_lastname(1000,1000,5,10);
fprintf(1,'simulation 2, fo = 1000, fs = 1000, Amplitude = 5, cycles = 10');
fprintf(1,'\n');
fprintf(1,'length of samples  ');
fprintf(1,'%d', length(samples));
fprintf(1,'\n');
fprintf(1,'hit the space bar to continue');
fprintf(1,'\n');
pause; % hit the space bar to continue

close all;

% Third simulation run: fo = 1000, fs = 8000, Amplitude = 5, cycles = 5.333
samples = cph2_lastname(1000,8000,5,5.333);
fprintf(1,'simulation 2, fo = 1000, fs = 8000, Amplitude = 5, cycles = 5.333');
fprintf(1,'\n');
fprintf(1,'length of samples  ');
fprintf(1,'%d', length(samples));
fprintf(1,'\n');
fprintf(1,'hit the space bar to continue');
fprintf(1,'\n');
pause; % hit the space bar to continue

close;



