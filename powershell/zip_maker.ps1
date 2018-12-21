
param(
    
    [Parameter(Mandatory=$true)]
    [string]$path,
    
    [Parameter(Mandatory=$true)]
    [string]$outpath,
    
    [Parameter(Mandatory=$true)]
    [int32]$maxsize
)

$usage = '
Usage:

zip_maker.ps1 -path[input path] -outpath[output path] -maxsize[zip size in Bytes] -debug[True/False]


'


$test = Test-Path -Path $outpath

if($test -eq 'True'){ echo 'Found Path' }

if($test -eq 'False'){mkdir $outpath 
echo 'Making Path' }

cd $path
$name = ls.name
$size = ls.length
$join = $name + '' + $size
if($debug -eq 'true'){echo $join}
$join | Out-File '\tmp\lstable.txt'