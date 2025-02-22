alter table eleve
add DATE_NAISSANCE DATE;

alter table eleve
add SEXE VARCHAR(10) NOT NULL DEFAULT 'FILLE',
ADD CONSTRAINT chk_sexe CHECK (SEXE IN ('FILLE', 'GARCON'));
