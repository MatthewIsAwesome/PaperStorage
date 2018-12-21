
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

zip_maker.ps1 -path[input path] -outpath[output path] -maxsize[zip size in KB] -debug[True/False]


'


$test = Test-Path -Path $outpath

if($test -eq 'True'){ echo 'Found Path' }

if($test -eq 'False'){mkdir $outpath 
echo 'Making Path' }

cd $path