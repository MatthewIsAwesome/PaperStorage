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

Remove-Item $PSScriptRoot\csv\maxlen.ini -Force -ErrorAction SilentlyContinue


$array = @()


#debug
#$path = D:\School\English

$FileList = Get-ChildItem -LiteralPath $path -File

$Results = foreach ($FL_Item in $FileList)
    {
    [PSCustomObject]@{
        Name = $FL_Item.Name
        Size_KB = '{0,7:N2}' -f ($FL_Item.Length / 1KB)
        }
    }

Remove-Item -Path \csv\sizes.csv -Force -ErrorAction SilentlyContinue
echo $Results

$Results | Export-Csv -Confirm -Force -Delimiter % -Path $PSScriptRoot\csv\results.csv
$maxsize | Out-File  -Path $PSScriptRoot\csv\maxlen.ini -Force

$match = 