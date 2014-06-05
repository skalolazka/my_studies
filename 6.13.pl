#!/usr/bin/perl

# rotate array by i positions
# solution: rotate by one, rotate by one again, ...

use strict;
use warnings;

package MyRotate;

sub new {
    return bless {} => shift;
}

sub rotate_by_one {
    my $arr = shift;
    my $prev = $arr->[-1]; # last element
    for (my $j = 0; $j < scalar(@$arr); $j++) {
        ($arr->[$j], $prev) = ($prev, $arr->[$j]);
    }
}

sub rotate {
    my $self = shift;
    my ($i, @arr) = @_;

    for (my $j = 0; $j < $i; $j++) {
        rotate_by_one(\@arr);
    }
    return @arr;
}

#print join(',', rotate(@ARGV))."\n";

package TestMyRotate;
use Test::More;
use Test::Deep;

my $module = MyRotate->new;
my @test_data = (
    { in => [0, 0], out => [0] },
    { in => [10, 0], out => [0] },
    { in => [1, 1, 0], out => [0, 1]}, 
    { in => [1, 0, 1, 2, 3], out => [3, 0, 1, 2,]}, 
    { in => [2, 0, 1, 2, 3], out => [2, 3, 0, 1]}, 
    { in => [2, 0, 1, 2, 3, 4], out => [3, 4, 0, 1, 2]}, 
    { in => [4, 0, 1, 2, 3, 4], out => [1, 2, 3, 4, 0]}, 
    { in => [5, 0, 1, 2, 3, 4], out => [0, 1, 2, 3, 4]}, 
);
for my $data (@test_data) {
    is_deeply([$module->rotate(@{$data->{in}})], $data->{out}, join(',', @{$data->{in}}).'OK');
}

done_testing;
