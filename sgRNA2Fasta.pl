#! /usr/bin/perl

use Cwd;

my $sgRNA_file1 = "Human GeCKOv2 Lib1 with UID.txt";
my $sgRNA_file2 = "Human GeCKOv2 Lib2 with UID.txt";

my $output = "GeCKO_lib.fa";

open OUT, ">$output" or die $!;
open SGRNA_1, "$sgRNA_file1" or die $!;
open SGRNA_2, "$sgRNA_file2" or die $!;

while (<SGRNA_1>){
	my $inline = $_;
	$inline=~s/\s+$//;
	next if $inline =~ /^target/;
	#print $inline,"\n";
	my @inputArray = split /\t/, $inline;
	#print pop(@inputArray);
	my $idLine = ">".join ("|",@inputArray[0..2]);
	if ($idLine=~ /\s/){
		#print $idLine,"\n";
		$idLine =~ s/\s/_/g;

	#exit;
	}
	print  OUT $idLine,"\n";
	my $seq = $inputArray[3];
	print OUT $seq,"\n";
	#exit;
}
close SGRNA_1;

while (<SGRNA_2>){
	my $inline = $_;
	$inline=~s/\s+$//;
	next if $inline =~ /^target/;
	#print $inline,"\n";
	my @inputArray = split /\t/, $inline;
	#print pop(@inputArray);
	my $idLine = ">".join ("|",@inputArray[0..2]);
	$idLine =~ s/\s/_/g;
	print OUT $idLine,"\n";
	my $seq = $inputArray[3];
	print OUT $seq,"\n";
	#exit;
}

close OUT;
close SGRNA_2;
