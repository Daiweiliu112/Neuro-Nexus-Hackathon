var correct = 0;
var incorrect = 0;
var ppPartial = 0;
var ppFull = 0;
var mp = 0;
var gp = 0;
var vepPartial = 0;
var vepFull = 0;
var vip = 0;
var i = 0;
var trial = 1;
var notes = "";

function setExport(filename, rows) {
        var processRow = function (row) {
            var finalVal = '';
            for (var j = 0; j < row.length; j++) {
                var innerValue = row[j] === null ? '' : row[j].toString();
                if (row[j] instanceof Date) {
                    innerValue = row[j].toLocaleString();
                };
                var result = innerValue.replace(/"/g, '""');
                if (result.search(/("|,|\n)/g) >= 0)
                    result = '"' + result + '"';
                if (j > 0)
                    finalVal += ',';
                finalVal += result;
            }
            return finalVal + '\n';
        };

        var csvFile = '';
        for (var i = 0; i < rows.length; i++) {
            csvFile += processRow(rows[i]);
        }

        var blob = new Blob([csvFile], { type: 'text/csv;charset=utf-8;' });
        if (navigator.msSaveBlob) { // IE 10+
            navigator.msSaveBlob(blob, filename);
        } else {
            var link = document.createElement("a");
            if (link.download !== undefined) { // feature detection
                // Browsers that support HTML5 download attribute
                var url = URL.createObjectURL(blob);
                link.setAttribute("href", url);
                link.setAttribute("download", filename);
                link.style.visibility = 'hidden';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }
        }
    }

// export the Csv
function exportCsv() {
    // if the last trial was not saved
    if (correct != 0 || incorrect != 0) {
        notes =  document.getElementById('notes').value;
        var trialData = [trial, 'bubblegum', correct, incorrect, ppFull, ppPartial, mp, gp, vepFull, vepPartial, vip, i, notes];
        gameData.push(trialData);
    }
    setExport('export.csv', gameData)
}

var gameData = [
    ['Trial','Game','Correct', 'Incorrect', 'PP Full', 'PP Partial', 'MP', 'GP', 'VEP Full', 'VEP Partial', 'VIP', 'I', 'Notes'],	
];

// reset
document.getElementById('reset').onclick = function() {
    document.getElementById("bubble").src="assets/games/game_images/bubble.png";
    notes =  document.getElementById('notes').value;
    var trialData = [trial, 'bubblegum', correct, incorrect, ppFull, ppPartial, mp, gp, vepFull, vepPartial, vip, i, notes];
    gameData.push(trialData);
    // reset variables
    trial++;
    correct = 0;
    incorrect = 0;
    ppPartial = 0;
    ppFull = 0;
    mp = 0;
    gp = 0;
    vepFull = 0;
    vepPartial = 0;
    vip = 0;
    i = 0;
    notes = "";
    document.getElementById('notes').value = "";
    document.getElementById('Remember Me').checked = false;
    document.getElementById('RememberMe').checked = false;
};


// count correct clicks
document.getElementById('Remember Me').onclick = function() {
    if (correct == 0)
        correct++;
    else 
        correct = 0;
    console.log(correct);
};

// count incorrect clicks
document.getElementById('RememberMe').onclick = function() {
    if (incorrect == 0)
        incorrect++;
    else 
        incorrect = 0;
};

// count pp partial
document.getElementById('ppPartial').onclick = function() {
    ppPartial++;
    console.log(ppPartial);
};

// count pp partial
document.getElementById('ppFull').onclick = function() {
    ppFull++;
    console.log(ppFull);
};


// count mp
document.getElementById('mp').onclick = function() {
    mp++;
};

// count gp
document.getElementById('gp').onclick = function() {
    gp++;
};

// count vep Full
document.getElementById('vepFull').onclick = function() {
    vepFull++;
};

// count vep partial
document.getElementById('vepPartial').onclick = function() {
    vepPartial++;
};

// count vip
document.getElementById('vip').onclick = function() {
    vip++;
};

// count i
document.getElementById('i').onclick = function() {
    i++;
};

// save button
document.getElementById('save').onclick = function() {
    //notes =  document.getElementById('notes').value;
};

