param(

    [Parameter(Mandatory=$true)]
    [string]$path,

    [Parameter(Mandatory=$true)]
    [string]$outpath,

    [Parameter(Mandatory=$true)]
    [int32]$maxsize,

    [Parameter(Mandatory=$false)]
    [int32]$bitforbitsplit,

    [switch]$debugger
)

$usage = '
Usage:

zip_maker.ps1 -path[input path] -outpath[output path] -maxsize[zip size in Bytes] -debugger[True/False]



'

Remove-Item $PSScriptRoot\tmp\maxlen.ini -Force -ErrorAction SilentlyContinue


$array = @()

if($bitforbitsplit -eq 1){
    Compress-Archive -DestinationPath $outpath -Path $path -CompressionLevel Optimal -Confirm

}else{



    $FileList = Get-ChildItem -LiteralPath $path -File

    $Results = foreach ($FL_Item in $FileList)
        {
        [PSCustomObject]@{
            Name = $FL_Item.Name
            Size_KB = '{0,7:N2}' -f ($FL_Item.Length / 1KB)
            }
        }

    Remove-Item -Path \CSV\sizes.csv -Force -ErrorAction SilentlyContinue
    echo $Results

    $Results | Export-Csv -Confirm -Force -Delimiter % -Path $PSScriptRoot\CSV\results.csv
    $maxsize | Out-File  -Path $PSScriptRoot\tmp\maxlen.ini -Force
    }


