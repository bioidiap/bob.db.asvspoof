

[Id, filename, attack, type] = textread('cm_develop.ndx', '%s %s %s %s');

fidreal = fopen('scores-dev-real', 'w');
fidattack = fopen('scores-dev-attack', 'w');

for i=1:length(attack)
    if strcmp(attack{i}, 'human') 
        fprintf(fidreal, '%s %s %s %f\n', Id{i}, Id{i}, filename{i}, Score(i));
    else
        fprintf(fidattack, '%s %s %s %f\n', Id{i}, Id{i}, filename{i}, Score(i));
    end
end
fclose(fidreal);
fclose(fidattack);