#!/usr/bin/perl

# rotate array by i positions
# solution: rotate by one, rotate by one again, ...

use strict;
use warnings;

package MyRotate;

sub new {
    return bless {} => shift;
}

sub reverse {
    my ($self, $arr, $start, $end) = @_;
    $start = 0 unless defined($start);
    $end = scalar(@$arr) - 1 unless defined($end);
    return if (!scalar(@$arr) || $start > $end || $end > scalar(@$arr));
    for (my $j = $start; $j <= $start + int(($end - $start) / 2); $j++) {
        my $rj = $end - $j + $start;
        ($arr->[$j], $arr->[$rj]) = ($arr->[$rj], $arr->[$j]);
    }
}

sub rotate {
    my ($self, $arr, $i) = @_;
    $i--;
    $self->reverse($arr, 0, $i);
    $self->reverse($arr, $i+1);
    $self->reverse($arr);
}


package TestMyRotate;
use Test::More;
use Test::Deep;

my $module = MyRotate->new;
my @test_data = (
    { in => [0], i => 0, out => [0] },
    { in => [0], i => 10, out => [0] },
    { in => [1, 0], i => 1, out => [0, 1]},
    { in => [0, 1, 2, 3], i => 1, out => [1, 2, 3, 0]},
    { in => [0, 1, 2, 3], i => 2, out => [2, 3, 0, 1]}, 
    { in => [0, 1, 2, 3, 4], i => 2, out => [2, 3, 4, 0, 1]}, 
    { in => [0, 1, 2, 3, 4], i => 4, out => [4, 0, 1, 2, 3]},
    { in => [0, 1, 2, 3, 4], i => 5, out => [0, 1, 2, 3, 4]},
    { in => [0, 1, 2, 3, 4, 5], i => 2, out => [2, 3, 4, 5, 0, 1]},
);
for my $data (@test_data) {
    $module->rotate($data->{in}, $data->{i});
    is_deeply($data->{in}, $data->{out}, join(',', @{$data->{in}}).' OK');
}

done_testing;
