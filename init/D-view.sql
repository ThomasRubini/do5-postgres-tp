CREATE VIEW VEtud AS
SELECT e.idel, e.nom, e.prenom, e.date_naissance, COUNT(idd) AS nbdevoirs
FROM eleve e
JOIN passage p ON e.idel = p.idel
GROUP BY e.idel, e.nom, e.prenom, e.date_naissance;
