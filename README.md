<img src="food-data-submarke_kombi.png" width="50%" alt="Logo">

# CHFDM - SwissFoodDataMediator

Diese Ontologie-Datei bildet die Basis für den Swiss Food Data Mediator. Sie verknüpft Daten aus verschiedenen Lebensmittel-Ontologien und erlaubt es so, SPARQL-Abfragen über diese verschiedenen Aspekte von Lebensmitteln laufen zu lassen.  

Gestartet wurde der CHFDM, um eine Datenbank für Proteinreiche Lebensmittel DaPro abzubilden. Diese hat zum Ziel, proteinreiche Alternative zu Fleischprodukten zu finden und zu analysieren.  

## Proprietäre Datenbanken

Einige der verlinkten Datenbanken sind (noch) nicht als offizielle Ontologie-Daten und SPARQL-Endpoints verfügbar. Diese werden für ZHAW-interne Projekte simuliert und an die Studierenden und Forschenden situativ abgegeben.  

# Installation / Verwendung

Um die Daten lokal anzuschauen, zu ergänzen oder zu verändern, empfehlen wir [Protégé](https://protege.stanford.edu/).  

Für unsere Browser-Applikationen verwenden wir einen **Apache Jena Fuseki**-Datenbankserver, der die SPARQL-Schnittstellen für die HTML/JS-Frontends bietet. Er kann von der [offiziellen Webseite heruntergeladen werden (zip, Apache Jena Fuseki 4.10.0)](https://dlcdn.apache.org/jena/binaries/apache-jena-fuseki-4.10.0.zip). Die "Installation" geschiet durch einfaches entpacken des zip-Files, z.B. nach "C:\Daten\JenaFuseki\".  

Voraussetzung daür ist eine Java-Umgebung, wir empfehlen das Open Java Development Kit (OpenJDK) **Amazon Corretto**. Es kann auf der [offiziellen Webseite heruntergeladen werden (Windows x64 msi, Version 21)](https://corretto.aws/downloads/latest/amazon-corretto-21-x64-windows-jdk.msi).  

Nachdem das OpenJDK installiert worden ist, kann der Apache Jena Fuseki mit der Batch-Datei **C:\Daten\JenaFuseki\fuseki-server.bat** gestartet werden. Er läuft fortan in einem Kommandozeilen-Fenster und kann darin mit ``[CTRL]`` + ``[C]`` (2x) gestoppt werden.  

Danach können die **Daten** von der zur Verfügung gestellten heruntergeladen (z.B. nach "C:\Daten\CHFDM-Daten\") und per [Interface](http://localhost:3030/#/) auf dem lokalen Datenbankserver geladen werden. Es wird dazu ein Dataset "DaPro" angelegt (["new dataset"](http://localhost:3030/#/manage/new)) in welches zu welchem die Daten hinzugefügt werden (["add data"](http://localhost:3030/#/dataset/DaPro/upload)). *Die Links gehen nur, wenn der lokale Server gestartet worden ist.*  

Wenn alles gut lief, kann bereits [das erste SPARQL-Query](http://localhost:3030/#/dataset/DaPro/query) abgesetzt werden:  

---  
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  
    PREFIX owl: <http://www.w3.org/2002/07/owl#>  
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>  
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>  
    PREFIX schema: <http://schema.org/>  
    PREFIX dapro: <http://dapro.opendata.zhaw.ch/DaPro.owl#>  
    SELECT * WHERE {  
      ?subject ?predicate ?object .  
    } LIMIT 10  
---  

Gratulation! Wir haben nun eine funktionierende Arbeitsumgebung.  

Jetzt können die **Interfaces** aus dem Ordner "C:\Daten\JenaFuseki\interface" aufgerufen werden. Dazu werden die .html-Dateien auf ein Browserfenster gezogen. Die Applikation läuft komplett lokal und verwendet den Apache-Jena-Fuseki-Server.

Alternativ kann die Schnittstelle per **python-Skript** angesprochen werden. Ein entsprechendes Demo-skript findet sich im Ordner C:\Daten\JenaFuseki\python


### Spielwiese intern

[github.io](https://zhaw-icls-data-management-visualization.github.io/CHFDM---SwissFoodDataMediator/index_githubio.htm) of this site
