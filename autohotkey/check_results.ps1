# output.txt file path is a required parameter
[CmdletBinding()]
param (
    [Parameter()]
    [string]
    $FilePath
)

if (-not($FilePath)) {
    Throw "You must specify a file"    
}

# Read file
$FileData = Get-Content .\autohotkey\output.txt


# Check to see if lines exist
if ($FileData.Length -ne 4) {
    Throw "$FilePath does not contain the correct number of lines (4)"
}

# Extract lines
$MultiCoreScore = $FileData[0]
$SingleCoreScore = $FileData[1]
$CoreCount = $FileData[2]
$EstimatedSingleCoreScore = $FileData[3]

# Split into text and values
$MultiCoreScoreText, $MultiCoreScoreValue = ($MultiCoreScore -Split (': '))
$SingleCoreScoreText, $SingleCoreScoreValue = ($SingleCoreScore -Split (': '))
$CoreCountText, $CoreCountValue = ($CoreCount -Split (': '))
$EstimatedSingleCoreScoreText, $EstimatedSingleCoreScoreValue = ($EstimatedSingleCoreScore -Split (': '))

# Check text side
$CheckText = $a, $b, $c, $d
$CheckText[0] = $MultiCoreScoreText, "Cinebench R23 Multi core Score"
$CheckText[1] = $SingleCoreScoreText, "Cinebench R23 Single core Score"
$CheckText[2] = $CoreCountText, "Number of Cores in This Machine"
$CheckText[3] = $EstimatedSingleCoreScoreText, "Cinebench R23 Estimated Single Core"

foreach ($Array in $CheckText) {
    $Actual, $Expected = $Array
    # CompareStrings($Expected, $Actual)   

    if ($Actual -ne $Expected) {
        Throw  "Expected: $Expected; Actual: $Actual"
    }
}

# Check value side
$CheckValue = $a, $b, $c, $d
$CheckValue[0] = $MultiCoreScoreValue
$CheckValue[1] = $SingleCoreScoreValue
$CheckValue[2] = $CoreCountValue
$CheckValue[3] = $EstimatedSingleCoreScoreValue

foreach ($Value in $CheckValue) {
    # $Value, $Type = $Array

    if ($Value -as [double] -isnot [double]) {
        Throw "'$Value' is not a number"
    } 

}

# Check estimation
if (
    # doing it this way bc [Math]::Round rounds down not up
    -not([string]::Format("{0:f2}", $MultiCoreScoreValue / $CoreCountValue) -eq $EstimatedSingleCoreScoreValue)
) {
    Throw "Estimated Single-Core values is incorrect"
}

Write-Output "$FilePath contains valid output"