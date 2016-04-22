<?php
$regions = array(40169=>"Benešov",40177=>"Beroun",40703=>"Blansko",40711=>"Brno-město",40720=>"Brno-venkov",40860=>"Bruntál",40738=>"Břeclav",40525=>"Česká Lípa",40282=>"České Budějovice",40291=>"Český Krumlov",40452=>"Děčín",40355=>"Domažlice",40878=>"Frýdek-Místek",40657=>"Havlíčkův Brod",40746=>"Hodonín",40568=>"Hradec Králové",40428=>"Cheb",40461=>"Chomutov",40614=>"Chrudim",40533=>"Jablonec nad Nisou",40771=>"Jeseník",40576=>"Jičín",40665=>"Jihlava",40304=>"Jindřichův Hradec",40436=>"Karlovy Vary",40886=>"Karviná",40185=>"Kladno",40363=>"Klatovy",40193=>"Kolín",40827=>"Kroměříž",40207=>"Kutná Hora",40541=>"Liberec",40479=>"Litoměřice",40487=>"Louny",40215=>"Mělník",40223=>"Mladá Boleslav",40495=>"Most",40584=>"Náchod",40894=>"Nový Jičín",40231=>"Nymburk",40789=>"Olomouc",40908=>"Opava",40916=>"Ostrava-město",40622=>"Pardubice",40673=>"Pelhřimov",40312=>"Písek",40380=>"Plzeň-jih",40371=>"Plzeň-město",40398=>"Plzeň-sever",40924=>"Praha",40240=>"Praha-východ",40258=>"Praha-západ",40321=>"Prachatice",40797=>"Prostějov",40801=>"Přerov",40266=>"Příbram",40274=>"Rakovník",40401=>"Rokycany",40592=>"Rychnov nad Kněžnou",40550=>"Semily",40444=>"Sokolov",40339=>"Strakonice",40631=>"Svitavy",40819=>"Šumperk",40347=>"Tábor",40410=>"Tachov",40509=>"Teplice",40606=>"Trutnov",40681=>"Třebíč",40835=>"Uherské Hradiště",40517=>"Ústí nad Labem",40649=>"Ústí nad Orlicí",40843=>"Vsetín",40754=>"Vyškov",40851=>"Zlín",40762=>"Znojmo",40690=>"Žďár nad Sázavou");

$cams = array();
$ch = curl_init();
$timeout = 5;
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36");

foreach ($regions as $rcode => $rname) {
    echo "$rname;";
    $url = "https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&verze=-1&z=T&f=TABULKA&nahled=N&sp=N&filtr=G~F_M~F_Z~F_R~F_P~_S~_null_null_&katalog=30853&pvo=ZAM09&zo=N&str=v171&c=v3~3__RP2015&u=v171__VUZEMI__101__$rcode";
    curl_setopt($ch, CURLOPT_URL, $url);
    $html = curl_exec($ch);
    $dom = new DOMDocument();
    @$dom->loadHTML($html);
    $cell2010 = $dom->getElementsByTagName('table')[2]->getElementsByTagName('tr')[14]->getElementsByTagName('span')[6]->nodeValue;
    $cell2012 = $dom->getElementsByTagName('table')[2]->getElementsByTagName('tr')[14]->getElementsByTagName('span')[8]->nodeValue;
    echo "$cell2010;$cell2012\n";
}

?>
