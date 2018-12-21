
param(
    
    [Parameter(Mandatory=$true)]
    [string]$path,
    
    [Parameter(Mandatory=$true)]
    [string]$outpath,
    
    [Parameter(Mandatory=$true)]
    [int32]$maxsize,

    [switch]$debugger
)

$usage = '
Usage:

zip_maker.ps1 -path[input path] -outpath[output path] -maxsize[zip size in Bytes] -debugger[True/False]



'

cd $path

$array = @()

$ls = ls
$name = $ls.Name

$path = D:\School\English

Get-ChildItem $path | ForEach-Object{
    $size += Get-ItemProperty.length 
}




cd $PSscriptRoot


if($debug -eq 'true'){echo $join}
echo $name #debug
$name | Out-File '$($PSScriptRoot)\tmp\lstable.txt'