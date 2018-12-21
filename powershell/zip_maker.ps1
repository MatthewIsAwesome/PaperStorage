
param(
    [string]$path,
    [string]$outpath,
    [int32]$maxsize,
    [boolean]$debug
)

$usage = '
Usage:

zip_maker.ps1 -path[input path] -outpath[output path] -maxsize[zip size in KB] -debug[True/False]


'

echo $usage
